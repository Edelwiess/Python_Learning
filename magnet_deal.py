import urllib.request
import urllib.parse
ip_tracker_url = 'https://ngosang.github.io/trackerslist/trackers_all_ip.txt'
http_tracker_url ='https://ngosang.github.io/trackerslist/trackers_all_http.txt'
remote_tracker_url = 'https://ngosang.github.io/trackerslist/trackers_best.txt'
get_remote_tracker_url = urllib.request.urlopen(http_tracker_url)
remote_tracker = get_remote_tracker_url.read()
remote_tracker = remote_tracker.decode('utf8')
remote_tracker = remote_tracker.split('\n\n')

remote_tracker.pop()
print(remote_tracker)

trackers=[]
trackerlist = 'udp://tracker.coppersurfer.tk:6969/announce,udp://tracker.opentrackr.org:1337/announce,udp://tracker.openbittorrent.com:80/announce,udp://9.rarbg.to:2710/announce,udp://9.rarbg.me:2710/announce,udp://exodus.desync.com:6969/announce,udp://tracker.cyberia.is:6969/announce,udp://tracker3.itzmx.com:6961/announce,udp://retracker.lanta-net.ru:2710/announce,http://tracker1.itzmx.com:8080/announce,udp://tracker.tiny-vps.com:6969/announce,udp://open.stealth.si:80/announce,udp://tracker.torrent.eu.org:451/announce,http://tracker4.itzmx.com:2710/announce,udp://tracker.moeking.me:6969/announce,udp://ipv4.tracker.harry.lu:80/announce,udp://bt1.archive.org:6969/announce,http://tracker.internetwarriors.net:1337/announce,udp://explodie.org:6969/announce,udp://bt2.archive.org:6969/announce'
#for each in (trackerlist.split(',')):
for each in (remote_tracker):
    encodedurl = urllib.parse.quote(each,safe='')
    trackers.append(encodedurl)

urlss = '&tr='.join(trackers)
#print(urlss)
#trackers_url = '&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2710%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2710%2Fannounce&tr=udp%3A%2F%2Fexodus.desync.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker3.itzmx.com%3A6961%2Fannounce&tr=udp%3A%2F%2Fretracker.lanta-net.ru%3A2710%2Fannounce&tr=http%3A%2F%2Ftracker1.itzmx.com%3A8080%2Fannounce&tr=udp%3A%2F%2Ftracker.tiny-vps.com%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=http%3A%2F%2Ftracker4.itzmx.com%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.moeking.me%3A6969%2Fannounce&tr=udp%3A%2F%2Fipv4.tracker.harry.lu%3A80%2Fannounce&tr=udp%3A%2F%2Fbt1.archive.org%3A6969%2Fannounce&tr=http%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fbt2.archive.org%3A6969%2Fannounce'

originallink = 'magnet:?xt=urn:btih:ec614c67629d81521b5926db3aaecef7080a561d&dn=Ralph.Breaks.the.Internet.2018.2160p.UHD.BluRay.X265.10bit.HDR.TrueHD.7.1.Atmos-TERMiNAL&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2900&tr=udp%3A%2F%2F9.rarbg.to%3A2750'
link1 = 'magnet:?xt=urn:btih:4EEEC8CFAE2F715B707231A4C022D3D545A6FA53&dn=Ralph.Breaks.The.Internet.2018.1080p.WEBRip.x264-MP4&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2920%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.pirateparty.gr%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.cyberia.is%3A6969%2Fannounce'
originallink = link1
newlink = '&tr='.join((originallink, urlss))
print(newlink)