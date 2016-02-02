VIDEO_PREFIX = "/video/aljazeera"

NAME = L('Title')

# make sure to replace artwork with what you want
# these filenames reference the example files in
# the Contents/Resources/ folder in the bundle
ART  = 'art-default.jpg'
ICON = 'icon-default.png'

####################################################################################################

def Start():

    ## make this plugin show up in the 'Video' section
    ## in Plex. The L() function pulls the string out of the strings
    ## file in the Contents/Strings/ folder in the bundle
    ## see also:
    ##  http://dev.plexapp.com/docs/mod_Plugin.html
    ##  http://dev.plexapp.com/docs/Bundle.html#the-strings-directory
    Plugin.AddPrefixHandler(VIDEO_PREFIX, VideoMainMenu, NAME, ICON, ART)

    Plugin.AddViewGroup("InfoList", viewMode="InfoList", mediaType="items")
    Plugin.AddViewGroup("List", viewMode="List", mediaType="items")

    ## set some defaults so that you don't have to
    ## pass these parameters to these object types
    ## every single time
    ## see also:
    ##  http://dev.plexapp.com/docs/Objects.html
    MediaContainer.title1 = NAME
    MediaContainer.viewGroup = "List"
    MediaContainer.art = R(ART)
    DirectoryItem.thumb = R(ICON)
    VideoItem.thumb = R(ICON)

    HTTP.CacheTime = CACHE_1HOUR




#### the rest of these are user created functions and
#### are not reserved by the plugin framework.
#### see: http://dev.plexapp.com/docs/Functions.html for
#### a list of reserved functions above



#
# Example main menu referenced in the Start() method
# for the 'Video' prefix handler
#

def VideoMainMenu():
    oc = ObjectContainer(title1='Menu')
    titre	= 'Live'
    thumb       = R(ICON)
    # This RMTP URL is not working as the player I tested (plex.tv, PHT or Roku) aren't able to play the stream
    #video_url   = 'rtmp://aljazeeraflashlivefs.fplive.net:443/aljazeeraflashlive-live?videoId=883816736001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId=/aljazeera_eng_med?videoId=883816736001&lineUpId=&pubId=665003303001&playerId=751182905001&affiliateId=%20&live=true'
    # URL found in the web source.
    # It looks like the ipad/iphone version
    video_url_m3u8 = 'http://aljazeera-eng-apple-live.adaptive.level3.net/apple/aljazeera/english/appleman.m3u8'
    rating_key  = 'live'
    art         = R(ART)
    summary     = 'Watch Al Jazeera Live'
    tagline	= 'Live'

    oc.add(
	VideoClipObject(
		key = Callback(Lookup, title=titre, thumb=thumb, rating_key=rating_key, url=video_url_m3u8, art=art, summary=summary, tagline=tagline),
		title=titre,
		tagline=tagline,
		rating_key =  rating_key,
		items = [
			MediaObject(
				parts = [PartObject(key=HTTPLiveStreamURL(Callback(PlayAJE, url=video_url_m3u8)))]
			)
		],
		summary=L(summary),
		thumb=thumb,
		art=art
	)
    )
    return oc


@route('/video/aljazeera/media')
def Lookup(title, thumb, rating_key, url, art, summary, tagline):
        Log.Debug("Entering Lookup")
        oc = ObjectContainer()
        oc.add(
                VideoClipObject(
                        key             = Callback(Lookup, title=title, thumb=thumb, rating_key=rating_key, url=url, art=art, summary=summary, tagline=tagline),
                        title           = title,
                        thumb           = thumb,
                        tagline         = tagline,
                        rating_key      = rating_key,
                        summary         = summary,
                        art             = art,
                        items           = [
                                MediaObject(
                                        parts = [PartObject(key=HTTPLiveStreamURL(Callback(PlayAJE, url=url)))]
                                )
                        ]
                )
        )

        return oc

@indirect
def PlayAJE(url):
        #return Redirect(url)
        return IndirectResponse(VideoClipObject, key=HTTPLiveStreamURL(url=url))
