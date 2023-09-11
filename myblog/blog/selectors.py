from blog.models import Category, Blog, Comment

#TODO Django model managers
'''
def add(*,x,y):
    return x+y

add(x=1,y=2)

example={
    "x" = 1
    "y" = 2
}

**example =(x=1, y=2)
add(**example)
'''


def get_categories(filter=None):
    '''
    Fetches all Blog category
    '''
    if not filter:
        categories = Category.objects.all()
        return categories
    
    if filter and isinstance(filter, dict):
        Category.objects.filter(**filter)

def get_specific_category(id:int) -> Category: 
    '''
    Returns an existing with the same ID
    '''
    category = Category.objects.get(pk=id)
    return category
     
def get_blog():
    all_blogs = Blog.objects.all()
    return all_blogs

def get_specific_blog(id:int):
    sp_blogs = Blog.objects.get(pk=id)
    return sp_blogs

 
def get_blog_comments(blog_id:int):
    comments = Comment.objects.filter(
        blog__id=blog_id
    )   
    return comments

def get_user_comments(user_id:int):
    sp_comments = Comment.objects.filter(
        sender__id=user_id
    )
    return sp_comments
    

'''
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ source blogenv/Scripts/activate
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip install pillow
Collecting pillow
  Using cached Pillow-10.0.0.tar.gz (50.5 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pillow
  Building wheel for pillow (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for pillow (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [205 lines of output]
'''

'''
     writing manifest file 'src\Pillow.egg-info\SOURCES.txt'
      running build_ext
     
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
     
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html

'''
'''
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ source blogenv/Scripts/activate
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip install pillow
Collecting pillow
  Using cached Pillow-10.0.0.tar.gz (50.5 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pillow
  Building wheel for pillow (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for pillow (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [205 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win32-cpython-311
      creating build\lib.win32-cpython-311\PIL
      copying src\PIL\BdfFontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BlpImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BmpImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BufrStubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ContainerIO.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\CurImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\DcxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\DdsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\EpsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ExifTags.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\features.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FitsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FliImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FpxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FtexImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GbrImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GdImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GifImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GimpGradientFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GimpPaletteFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GribStubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Hdf5StubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IcnsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IcoImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Image.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageChops.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageCms.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageColor.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageDraw.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageDraw2.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageEnhance.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFilter.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFont.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageGrab.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMath.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMode.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMorph.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageOps.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImagePalette.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImagePath.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageQt.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageSequence.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageShow.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageStat.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageTk.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageTransform.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageWin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImtImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IptcImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Jpeg2KImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\JpegImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\JpegPresets.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\McIdasImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MicImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MpegImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MpoImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MspImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PaletteFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PalmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcdImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcfFontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PdfImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PdfParser.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PixarImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PngImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PpmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PsdImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PSDraw.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PyAccess.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\QoiImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SgiImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SpiderImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SunImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TarIO.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TgaImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TiffImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TiffTags.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WalImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WebPImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WmfImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XbmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XpmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XVThumbImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_binary.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_deprecate.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_tkinter_finder.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_util.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_version.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\__init__.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\__main__.py -> build\lib.win32-cpython-311\PIL
      running egg_info
      writing src\Pillow.egg-info\PKG-INFO
      writing dependency_links to src\Pillow.egg-info\dependency_links.txt
      writing requirements to src\Pillow.egg-info\requires.txt
      writing top-level names to src\Pillow.egg-info\top_level.txt
      reading manifest file 'src\Pillow.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no files found matching '*.c'
      warning: no files found matching '*.h'
      warning: no files found matching '*.sh'
      warning: no files found matching '*.txt'
      warning: no previously-included files found matching '.appveyor.yml'
      warning: no previously-included files found matching '.clang-format'
      warning: no previously-included files found matching '.coveragerc'
      warning: no previously-included files found matching '.editorconfig'
      warning: no previously-included files found matching '.readthedocs.yml'
      warning: no previously-included files found matching 'codecov.yml'
      warning: no previously-included files found matching 'renovate.json'
      warning: no previously-included files matching '.git*' found anywhere in distribution
      warning: no previously-included files matching '*.so' found anywhere in distribution
      no previously-included directories found matching '.ci'
      adding license file 'LICENSE'
      writing manifest file 'src\Pillow.egg-info\SOURCES.txt'
      running build_ext
     
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
      
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html
     
      Traceback (most recent call last):
        File "<string>", line 988, in <module>
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\__init__.py", line 103, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\core.py", line 185, in setup       
          return run_commands(dist)
                 ^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\core.py", line 201, in run_commands          dist.run_commands()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 969, in run_commands          self.run_command(cmd)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\wheel\bdist_wheel.py", line 364, in run
          self.run_command("build")
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\command\build.py", line 131, in run          self.run_command(cmd_name)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command  
          self.distribution.run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\command\build_ext.py", line 88, in run        
          _build_ext.run(self)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 345, in run
          self.build_extensions()
        File "<string>", line 811, in build_extensions
      RequiredDependencyException: zlib
     
      During handling of the above exception, another exception occurred:
     
      Traceback (most recent call last):
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 351, in <module>
          main()
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 333, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 249, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-install-ia0srdkn\pillow_32ac6acccbda4496a48e9076d7ec61fe\_custom_build\backend.py", line 53, in build_wheel
          return super().build_wheel(wheel_directory, config_settings, metadata_directory)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\build_meta.py", line 434, in build_wheel      
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\build_meta.py", line 419, in _build_with_temp_dir
          self.run_setup()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-install-ia0srdkn\pillow_32ac6acccbda4496a48e9076d7ec61fe\_custom_build\backend.py", line 47, in run_setup
          return super().run_setup(setup_script)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ht6xlcnq\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in run_setup
          exec(code, locals())
        File "<string>", line 1005, in <module>
      RequiredDependencyException:
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
     
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html
     
     
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build pillow
ERROR: Could not build wheels for pillow, which is required to install pyproject.toml-based projects

[notice] A new release of pip available: 22.3.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip uninstall wheel
Found existing installation: wheel 0.41.2
Uninstalling wheel-0.41.2:
  Would remove:
    c:\users\elitebook\onedrive\desktop\django course\backend\learning_django\blogenv\lib\site-packages\wheel-0.41.2.dist-info\*
    c:\users\elitebook\onedrive\desktop\django course\backend\learning_django\blogenv\lib\site-packages\wheel\*
    c:\users\elitebook\onedrive\desktop\django course\backend\learning_django\blogenv\scripts\wheel.exe
Proceed (Y/n)? y
  Successfully uninstalled wheel-0.41.2
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip install wheel
Collecting wheel
  Using cached wheel-0.41.2-py3-none-any.whl (64 kB)
Installing collected packages: wheel
Successfully installed wheel-0.41.2

[notice] A new release of pip available: 22.3.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip uninstall pillow
WARNING: Skipping pillow as it is not installed.
(blogenv) 
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$ pip install pillow
Collecting pillow
  Using cached Pillow-10.0.0.tar.gz (50.5 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: pillow
  Building wheel for pillow (pyproject.toml) ... error
  error: subprocess-exited-with-error
  
  × Building wheel for pillow (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [205 lines of output]
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build\lib.win32-cpython-311
      creating build\lib.win32-cpython-311\PIL
      copying src\PIL\BdfFontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BlpImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BmpImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\BufrStubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ContainerIO.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\CurImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\DcxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\DdsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\EpsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ExifTags.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\features.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FitsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FliImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FpxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\FtexImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GbrImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GdImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GifImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GimpGradientFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GimpPaletteFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\GribStubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Hdf5StubImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IcnsImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IcoImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Image.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageChops.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageCms.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageColor.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageDraw.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageDraw2.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageEnhance.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFilter.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageFont.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageGrab.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMath.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMode.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageMorph.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageOps.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImagePalette.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImagePath.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageQt.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageSequence.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageShow.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageStat.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageTk.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageTransform.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImageWin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\ImtImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\IptcImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\Jpeg2KImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\JpegImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\JpegPresets.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\McIdasImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MicImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MpegImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MpoImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\MspImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PaletteFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PalmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcdImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcfFontFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PcxImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PdfImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PdfParser.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PixarImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PngImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PpmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PsdImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PSDraw.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\PyAccess.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\QoiImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SgiImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SpiderImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\SunImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TarIO.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TgaImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TiffImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\TiffTags.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WalImageFile.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WebPImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\WmfImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XbmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XpmImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\XVThumbImagePlugin.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_binary.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_deprecate.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_tkinter_finder.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_util.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\_version.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\__init__.py -> build\lib.win32-cpython-311\PIL
      copying src\PIL\__main__.py -> build\lib.win32-cpython-311\PIL
      running egg_info
      writing src\Pillow.egg-info\PKG-INFO
      writing dependency_links to src\Pillow.egg-info\dependency_links.txt
      writing requirements to src\Pillow.egg-info\requires.txt
      writing top-level names to src\Pillow.egg-info\top_level.txt
      reading manifest file 'src\Pillow.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no files found matching '*.c'
      warning: no files found matching '*.h'
      warning: no files found matching '*.sh'
      warning: no files found matching '*.txt'
      warning: no previously-included files found matching '.appveyor.yml'
      warning: no previously-included files found matching '.clang-format'
      warning: no previously-included files found matching '.coveragerc'
      warning: no previously-included files found matching '.editorconfig'
      warning: no previously-included files found matching '.readthedocs.yml'
      warning: no previously-included files found matching 'codecov.yml'
      warning: no previously-included files found matching 'renovate.json'
      warning: no previously-included files matching '.git*' found anywhere in distribution
      warning: no previously-included files matching '*.so' found anywhere in distribution
      no previously-included directories found matching '.ci'
      adding license file 'LICENSE'
      writing manifest file 'src\Pillow.egg-info\SOURCES.txt'
      running build_ext
     
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
     
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html
     
      Traceback (most recent call last):
        File "<string>", line 988, in <module>
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\__init__.py", line 103, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\core.py", line 185, in setup       
          return run_commands(dist)
                 ^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\core.py", line 201, in run_commands          dist.run_commands()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 969, in run_commands          self.run_command(cmd)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\wheel\bdist_wheel.py", line 364, in run
          self.run_command("build")
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\command\build.py", line 131, in run          self.run_command(cmd_name)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command  
          self.distribution.run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\dist.py", line 1001, in run_command
          super().run_command(command)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command 
          cmd_obj.run()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\command\build_ext.py", line 88, in run        
          _build_ext.run(self)
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 345, in run
          self.build_extensions()
        File "<string>", line 811, in build_extensions
      RequiredDependencyException: zlib
     
      During handling of the above exception, another exception occurred:
     
      Traceback (most recent call last):
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 351, in <module>
          main()
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 333, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\OneDrive\Desktop\Django course\BackEnd\learning_django\blogenv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py", line 249, in build_wheel
          return _build_backend().build_wheel(wheel_directory, config_settings,
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-install-4e7n80bz\pillow_898339695cf143aa99aa0c410461ba30\_custom_build\backend.py", line 53, in build_wheel
          return super().build_wheel(wheel_directory, config_settings, metadata_directory)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\build_meta.py", line 434, in build_wheel      
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\build_meta.py", line 419, in _build_with_temp_dir
          self.run_setup()
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-install-4e7n80bz\pillow_898339695cf143aa99aa0c410461ba30\_custom_build\backend.py", line 47, in run_setup
          return super().run_setup(setup_script)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\Elitebook\AppData\Local\Temp\pip-build-env-ecmhwep5\overlay\Lib\site-packages\setuptools\build_meta.py", line 341, in run_setup        
          exec(code, locals())
        File "<string>", line 1005, in <module>
      RequiredDependencyException:
     
      The headers or library files could not be found for zlib,
      a required dependency when compiling Pillow from source.
     
      Please see the install instructions at:
         https://pillow.readthedocs.io/en/latest/installation.html
     
     
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pillow
Failed to build pillow
ERROR: Could not build wheels for pillow, which is required to install pyproject.toml-based projects

[notice] A new release of pip available: 22.3.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
(blogenv)
Elitebook@DESKTOP-PFSQFAA MINGW32 ~/OneDrive/Desktop/Django course/BackEnd/learning_django
$
'''


