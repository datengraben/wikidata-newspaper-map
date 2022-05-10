#
# Prints out a table to display all relations from newspapers to nuts areas
#
import pandas as pd

df = pd.read_csv('zeitungen-mit-nuts.csv')


def header(cols):
    print("<thead>")
    print("<tr>")
    for c in cols:
        print("  <th>{}</th>".format(c))
    print("</tr>")
    print("</thead>")


def row(cols):
    print("<tr>")
    for c in cols:
        print("  <td>{}</td>".format(c))
    print("</tr>")


def link(name, href):
    return '{} <a href="{}"><img alt="Wikidata-logo.svg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/20px-Wikidata-logo.svg.png" decoding="async" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/30px-Wikidata-logo.svg.png 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Wikidata-logo.svg/40px-Wikidata-logo.svg.png 2x" data-file-width="1050" data-file-height="590" width="20" height="11"></a>'.format(name, href)


print('<table id="example" class="table table-striped" style="width:100%">')
header(['zeitung', 'nuts3', 'nuts3-name'])
print("<tbody>")

for e in df.values:
    row([link(e[2], e[1]), e[3], link(e[4], e[5])])

print("</tbody>")
print("</table>")
