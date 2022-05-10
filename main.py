#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Aggregates newspaper data from wikidata download and also appends changelog markdown to
a markdown file

Usage:
  main.py [--dry-run] [--verbose | --quiet]
  main.py (-h | --help)
  main.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --dry-run     Only process input, don't write result files
  -v --verbose  Show really all the output
  -q --quiet    Don't show any output, except its an error
"""

#
# This creates 
#  1. A file with nuts areas and the count of newspapers that are writing their
#  2. A file with all matches from newspaper to nuts3 code area (which will be used to create a html page)
#  3. Changelog/Diff from the last version, so a user can see what data is new or deleted after a rebuild
#

from datetime import date, datetime
from genericpath import exists
import pandas as pd
from docopt import docopt


def get_different_rows(old=None, new=None):
    """ 
    Computes a dataframe with only the different rows
    """
    old['source'] = 'alt - entfernt  '
    new['source'] = 'neu - hinzgefügt'
    different_rows = pd.concat([old, new])[["zeitung", "zeitungLabel", "nuts", "popLabel", "pop", "source"]].drop_duplicates(keep=False, subset=["zeitung", "zeitungLabel", "nuts", "popLabel", "pop"])

    if not arguments['--quiet']:
        print("Get differnt rows")
        print(" * {} old rows".format(len(old)))
        print(" * {} new rows".format(len(new)))
        print(" * diff rows = {}".format(len(different_rows)))
    
    if arguments['--verbose']:
        print(different_rows)

    return different_rows

def startsWithOneOf(elem, matchingItems):
    for item in matchingItems:
        if elem.startswith(item):
            return True
    return False

def nutsed(ppath):
    """
    Creates generic data frame from raw wikidata query response
    """
    data = pd.read_csv(ppath)

    if arguments['--verbose']:
        print("Read {} lines of data".format(len(data)))

    nuts_papers = data[['zeitung', 'zeitungLabel', 'popLabel', 'nuts', 'pop']].drop_duplicates()

    nuts_papers = nuts_papers[False == nuts_papers['zeitungLabel'].apply(lambda row: startsWithOneOf(row, ['Handelsblatt', 'die tageszeitung', 'Bild', 'Die Welt', 'junge Welt']))]

    # Join with nuts data
    if not arguments['--quiet']:
        # Create report
        # How many newspapers are retrieved
        print("  Numbers of newspapers overall: \t{}".format(len(data['zeitungLabel'].unique())))
        # How many newspapers are fully annotated
        # Haw many are sufficently annotated?
        #  * Every newspaper that has at least one nuts3-area from "place of publication"
        print("      * sufficently annotated:   \t{}".format(len(data['zeitungLabel'].unique())))
        print("")
        print("  Number of 5-digit NUTS regions:\t{}".format(len(data['nuts'].unique())))
        print("")
        print("  Relevant rows to plot:         \t{}".format(len(nuts_papers)))
        # Not sufficient are the newspapers that have on nuts3-code from their headquater
        # Not annotated are the newspapers that have no nuts3-code from anything, maybe only the country

        # How many are probable interesting, but not sufficently annotated? (Maybe to hard, we don't know what we don't know)

    return nuts_papers

def summary(sourcedf):
    if arguments['--verbose']:
        print("")
        print(" = SUMMARY OF DATA = ")  
        print(sourcedf)
        print("")
        print("")

if __name__ == '__main__':
    arguments = docopt(__doc__, version='main.py 0.5')
    # print(arguments)

    if not arguments['--quiet']:
        print("")
        print("")
        print("=== First source - depicts =")
    nuts_papers = nutsed('data/test.data.csv')
    nuts_counts = nuts_papers.groupby(['nuts']).count()
    summary(nuts_counts)
    if not arguments['--dry-run']:
        nuts_counts.to_csv('data/nuts-count.csv')

    if not arguments['--quiet']:
        print("")
        print("")
        print("=== Second source - headquarters ========")
    nuts_papers_hq = nutsed('data/test-hq.data.csv')
    nuts_counts_hq = nuts_papers_hq.groupby(['nuts']).count()
    summary(nuts_counts_hq)
    if not arguments['--dry-run']:
        nuts_counts_hq.to_csv('data/nutshq-count.csv')

    if not arguments['--quiet']:
        print("")
        print("")
        print("=== Third source - headquarters from local newspapers ========")
    nuts_papers_hq2 = nutsed('data/test-hq2.data.csv')
    nuts_counts_hq2 = nuts_papers_hq2.groupby(['nuts']).count()
    summary(nuts_counts_hq2)
    if not arguments['--dry-run']:
        nuts_counts_hq2.to_csv('data/nutshq2-count.csv')


    # Temporary 
    if not arguments['--quiet']:
        print("")
        print("")
        print("=== Fourth source (temporary) - place of publication (old) ========")
    nuts_papers_p291 = nutsed('data/test-p291.data.csv')
    nuts_counts_p291 = nuts_papers_p291.groupby(['nuts']).count()
    summary(nuts_counts_p291)
    if not arguments['--dry-run']:
        nuts_counts_p291.to_csv('data/nuts-p291-count.csv')

    
    if not arguments['--quiet']:
        print("")
        print("")
        print("=== Fourth source (temporary) - place of publication (old) ========")
    nuts_papers_bdzv = nutsed('data/all_bdzv_papers_with_location_properties.data.csv')
    nuts_counts_bdzv = nuts_papers_bdzv.groupby(['nuts']).count()
    summary(nuts_counts_bdzv)
    if not arguments['--dry-run']:
        nuts_counts_bdzv.to_csv('data/nuts-bdzv-count.csv')




    if not arguments['--quiet']:
        print("")
        print("")
        print("Merged contents ======================")
    merged = pd.concat([nuts_papers, nuts_papers_hq, nuts_papers_hq2, nuts_papers_p291, nuts_papers_bdzv], ignore_index=True)
    result = merged[['zeitung', 'zeitungLabel', 'nuts', 'popLabel', 'pop']].drop_duplicates()

    # Compute difference and print to csv
    #  then write new result csv to outfile
    if exists('zeitungen-mit-nuts.csv'):
        nutspapers_old = pd.read_csv('zeitungen-mit-nuts.csv')
        different_rows = get_different_rows(old=nutspapers_old, new=result)
        different_rows = different_rows.sort_values(by='zeitungLabel')
        # print(different_rows.columns)

        if arguments['--verbose']:
            print(different_rows)
            print("Len of different rows ", len(different_rows))

        if len(different_rows) > 0:
            print("-> Write to changelog ...")
            with open('generated-changelog.md', 'w+') as fp:
                today = datetime.now().date()
                fp.write("Aktualisiert am {} mit {} Zeilen neuer Zeitung-zu-NUTS3 Zuordnung:\n\n".format(today, len(different_rows)))

                last_name = ""
                for row in different_rows.values:
                    print("Printing row ...")
                    link = row[0]
                    name = row[1]
                    region_name = row[3]
                    nuts3 = row[2]
                    region_link = row[4]
                    source = row[5]

                    # Extract entity
                    entity = link[link.rfind("/") + 1:]

                    if row[1] != last_name:
                        fp.write("  * Zeitung [{}]({}) - direkt zur [Versionsgeschichte](https://www.wikidata.org/w/index.php?title={}&action=history)\n".format(name, link, entity))
                        fp.write("    - {} [Gebiet {}]({}) ({})\n".format(source, region_name, region_link, nuts3))
                    else:
                        fp.write("    - {} [Gebiet {}]({}) ({})\n".format(source, region_name, region_link, nuts3))

                    last_name = name
                fp.write("\n")
        else:
            print("-> No changelog")

    if not arguments['--dry-run']:
        result.sort_values(by=['zeitungLabel', 'nuts']).to_csv('zeitungen-mit-nuts.csv')

    result_count = result[['zeitungLabel', 'nuts', 'popLabel']].groupby(['nuts', 'popLabel']).count()
    
    if not arguments['--dry-run']:
        result_count.sort_values(by=['zeitungLabel', 'nuts']).to_csv('nuts-merged-count.csv')
    #print(result)

    if not arguments['--quiet']:
        print("Done. Merged to {} rows".format(len(result)))
