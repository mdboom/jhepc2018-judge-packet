import csv
import os
import sys

with open(sys.argv[-1]) as fd:
    with open('source/index.rst', 'w') as index:
        index.write('John Hunter Excellence in Plotting Contest 2018\n')
        index.write('-----------------------------------------------\n')
        index.write('\n')
        index.write('.. raw:: html\n\n')

        reader = csv.reader(fd)
        for i, row in enumerate(reader):
            if i == 0:
                continue
            with open(f'source/entry{i}.rst', 'w') as out:
                w = out.write
                w(f'Entry {i}\n')
                w('=========\n')
                w('\n')
                w(f'{row[3]}\n')
                w('------------------------------------------------------------\n')
                w('\n')
                w(f'{row[2]}\n\n')

                for ext in ['.png', '.gif']:
                    if os.path.exists(f'images/entry{i}{ext}'):
                        w('.. raw:: html\n\n')
                        w(f'    <img width=640 src="entry{i}{ext}"/>\n\n')
                for ext in ['.mp4', '.mov', '.avi']:
                    if os.path.exists(f'images/entry{i}{ext}'):
                        w('.. raw:: html\n\n')
                        w(f'    <video width=640 controls><source src="entry{i}{ext}"/></video>\n\n')
                        w(f'If the video does not play above, try downloading `from this link <entry{i}{ext}>`__.\n\n')
                w('\n')
                w(row[4])
                w('\n')
                links = []
                if row[6]:
                    links.append(row[6])
                if row[7]:
                    links.append(row[7])
                w('\n\n')
                w("**Code and data:** {}".format(
                    ', '.join(f'`{i+1} <{x}>`__' for i, x in enumerate(links))))

                index.write(f'    <a href="entry{i}.html"><img alt="Entry {i}" src="thumb.entry{i}.png"/></a>\n')
