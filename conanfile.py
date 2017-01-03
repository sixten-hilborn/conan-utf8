from conans import ConanFile
from conans.tools import get

class Utf8CppConan(ConanFile):
    name = "UTF8-CPP"
    version = "2.3.4"
    description = 'UTF-8 with C++ in a Portable Way'
    folders = []
    settings = None
    generators = "cmake"
    url = "http://utfcpp.sourceforge.net/"
    license = "Free - see utf8.h"

    def source(self):
        get("https://sourceforge.net/projects/utfcpp/files/utf8cpp_2x/Release%202.3.4/utf8_v2_3_4.zip/download")

    def build(self):
		pass
        
    def package(self):
        self.copy(pattern="*.h", dst="include", src="source")

    def package_info(self):
        pass
