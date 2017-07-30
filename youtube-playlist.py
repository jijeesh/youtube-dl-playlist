import sys
import os


class PlaylistDownloader:
    targetDir = './'
    totalVideos = 0
    downloaded = 0
    def setTarget(self,target):
        self.targetDir = os.path.realpath(target)
        return self.targetDir
    def downloadVideos(self,playlistURL):
        print("Your Play List is : " + playlistURL)
        option = self.targetDir + '/%\(title\)s-%\(id\)s.%\(ext\)s'

        try:
            #os.system('youtube-dl  -cit ' + playlistURL)
            os.system('youtube-dl -o %s %s' % (option , playlistURL))
            return True
        except KeyboardInterrupt:
            sys.exit(1)
        except Exception as e:
            print("Failed : " , e.strerror)
            return False




if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: youtube-dl-playlist PLAYLIST_URL [DESTINATION_PATH]')
        sys.exit(1)
    else:
        print(len(sys.argv) )
        print("Playlist URL:" + sys.argv[1])
        print("Destination Path: " + sys.argv[2])
        obj = PlaylistDownloader()

        if len(sys.argv) == 3:
            obj.setTarget(sys.argv[2])
            print("New target: " + obj.targetDir)
        else:
            print("Default Target: " + obj.targetDir)

        obj.downloadVideos(sys.argv[1])


