import tools
import logger
import streamClasses
import wget
import sys

# Accept command line arguments for url
def main( baseURL = None ):

  if baseURL is None:
    return

  for i in range(1, 10):
    url = baseURL + '/tvshows/' + str(i)
    filename = wget.download(url, 'm3u/collection' + str(i))
    apollolist = streamClasses.rawStreamList(filename)

  url = baseURL + '/movies/'
  filename = wget.download(url, 'm3u')
  apollomovies = streamClasses.rawStreamList(filename)



if __name__ == "__main__":
  if len(sys.argv) > 1:
    main(sys.argv[1])
  else:
    main()
  print('done')
  sys.exit()