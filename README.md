AlJazeera.bundle
================

#### FORKED FROM: [https://github.com/lotooo/AlJazeera.bundle](https://github.com/lotooo/AlJazeera.bundle)

#### This fork adds support for iOS devices and also enables HD Live stream. Credit for the original channel goes to [lotooo](https://github.com/lotooo).

#### For the HD stream, makes use of [youtube-dl](https://github.com/rg3/youtube-dl). See instructions below (this is optional and a lower quality stream will be used as a fallback)

---

Channel to watch Al Jazeera live from Plex


## Installation with git

```bash
  cd $PLEX_FOLDER/Plug-ins
  git clone https://github.com/vin047/AlJazeera.bundle.git
  # For HD playback, do the following:
  cd AlJazeera.bundle
  git submodule init
  git submodule update
```

To update the plugin:

```bash
  cd $PLEX_FOLDER/Plug-ins/AlJazeera.bundle
  git pull
  # If you're using the HD stream:
  git submodule update
```

## Manual installation without git

* Download zip file from here: https://github.com/vin047/AlJazeera.bundle/releases/latest
* Unzip the file
* Move the unzipped bundle to $PLEX_FOLDER/Plug-ins

To update the plugin:

* Redownload the zip file and replace the .bundle file
