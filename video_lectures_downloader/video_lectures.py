"""Given a video lectures URL this will download all clips into the specified directory.

Must have mencoder installed on the system.  Downloads each clip in parallel.

Usage:
python video_lectures.py <video_lectures_url> <output_dir>

Example:
python video_lectures.py http://videolectures.net/cikm08_elkan_llmacrf/ elkan
"""

import multiprocessing
import os
import re
import subprocess
import sys
import urllib


def stream_wmv(url, out_file):
    cmd = 'mencoder %s -o %s -ovc copy -oac copy' % (url, out_file)
    subprocess.call(cmd.split())

def main(vl_url, output_dir):
    url_data = urllib.urlopen(vl_url).read()
    wmv_url = re.search('(mms://.*\.wmv)', url_data).group(1)[:-6]
    video_nums = map(int, re.findall("setvideo\('([0-9]+)'\)", url_data))
    videos = [('%s%.2d.wmv' % (wmv_url, x), '%s/%d.avi' % (output_dir, x))
              for x in video_nums]
    print(videos)
    try:
        os.mkdir(output_dir)
    except OSError:
        pass
    procs = [multiprocessing.Process(target=stream_wmv, args=x) for x in videos]
    for x in procs:
        x.start()
    for x in procs:
        x.join()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    main(*sys.argv[1:])
