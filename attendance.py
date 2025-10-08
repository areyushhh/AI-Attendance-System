# Simple attendance CSV logger demo (no face recognition to keep small)
import csv, datetime, sys
DB='attendance.csv'
def mark(name):
    with open(DB,'a',newline='') as f:
        w=csv.writer(f); w.writerow([name, datetime.datetime.now().isoformat()])
    print('Marked present for',name)
if __name__=='__main__':
    if len(sys.argv)<2:
        print('Usage: python attendance.py YourName')
    else:
        mark(sys.argv[1])
