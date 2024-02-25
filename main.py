import tools
import logger
import streamClasses
import wget
import sys

# Accept command line arguments for url
def main( url = None ):

  '''for i in range(20):
    url = baseurl + str(i)
    print(wget.download(url, ('m3u/apollotvshows-'+str(i)+'.m3u')))
    apollolist = streamClasses.rawStreamList('m3u/apollotvshows-'+str(i)+'.m3u')'''

  filename = wget.download(url, 'm3u')
  print(filename) #if not downloading comment out this line.
  apollomovies = streamClasses.rawStreamList(filename)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    main()
  print('done')
  sys.exit()