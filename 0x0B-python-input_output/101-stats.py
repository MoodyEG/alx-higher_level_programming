#!/usr/bin/python3
""" Main Module """
import sys

class Stats:
    """ Class Stats that provide info """
    def __init__(self):
        self.dic = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
        self.size = 0

    def add_status(self, status):
        """ Increase the stack on the status """
        if status in self.dic:
            self.dic[status] += 1

    def print_stats(self):
        """ Print stats """
        print("File size: {}".format(self.size))
        for key in sorted(self.dic.keys()):
            if self.dic[key] != 0:
                print("{}: {:d}".format(key, self.dic[key]))

if __name__ == "__main__":
    stats = Stats()
    line_num = 0
    try:
        for line in sys.stdin:
            if line_num % 10 == 0 and line_num != 0:
                stats.print_stats()
            try:
                line_list = [x for x in line.split(" ") if x.strip()]
                stats.add_status(line_list[-2])
                stats.size += int(line_list[-1].strip("\n"))
            except ValueError:
                pass
            line_num += 1
    except KeyboardInterrupt:
        stats.print_stats()
        raise
    stats.print_stats()
