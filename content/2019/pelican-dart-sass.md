title: Getting webassets to work with Dart Sass
tags: code
date: 2019-07-05


The Ruby version of Sass has been deprecated, but is
readily replaced with the Dart implementation.

    $ brew install dart
    $ brew install sass

Now the `sass` command will work pretty much the same as
it did with the Ruby version.

However, some libraries that are based on the Ruby version
may not work, as some options have been changed.

This was the case for using the webassets Python package
with [Pelican](https://blog.getpelican.com).

With dart-sass version 1.20.1 and webassets version 0.12.1, I
got the following error:

    Caught exception "FilterError: sass: subprocess returned
    a non-success result code: 64, stdout=b'Could not find an 
    option named "cache-location". [...]

To bypass the `cache-location` option, you need to comment out a few lines of code.

Open the file `<python env>/site-packages/webassets/filter/sass.py`, where `<python env>` is the path to your environment. In my case, it's in my `virtualenv`s directory.

With that file open, comment out lines 164-170:

    # if isinstance(self.ctx.cache, FilesystemCache):
    #     args.extend(['--cache-location',
    #                  os.path.join(orig_cwd, self.ctx.cache.directory, 'sass')])
    # elif not cd:
    #     # Without a fixed working directory, the location of the cache
    #     # is basically undefined, so prefer not to use one at all.
    #     args.extend(['--no-cache'])

Now you should be able to use the `assets` plugin for Pelican without issue.
