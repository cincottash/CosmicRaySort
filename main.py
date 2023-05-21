import time
import random

def miracleSort(unsortedList):
  print(f'Unsorted list:{unsortedList}\n')
  while(unsortedList != sorted(unsortedList)):
    print('Waiting for cosmic ray...\n')
    time.sleep(1)

  print(f'A cosmic ray has sorted the list!\nSorted list:{unsortedList}')

def main():
  myList = [random.randint(0, 10) for x in range(10)]
  miracleSort(myList)

if __name__ == '__main__':
  main()
