import idaapi
import ida_kernwin
import ida_nalt
import idautils
import idc
import os
import function_locator
import importlib
from collections import defaultdict, deque
from elftools.elf.elffile import ELFFile

icon = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8\x00\x00\x00\xc8\x08\x06\x00\x00\x00\xadX\xae\x9e\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x0cZIDATx^\xed\x9d\xfb}\xd4:\x10\x85\xa5\xd4s\xb9-\x005@\rp\xbb\x08\xdb\x05\xa4\x86\xa4\x86,-\x10\xea\x89\xefO\xebx\xd7\xf1z\xad\x875\xa3\x19\xcd\xe1O\xa2\x87u4\x9f\xceH~\xacw\xf8\x07\x05\xa0\xc0M\x05<\xb4\x81\x02P\xe0\xb6\x02\x00\x04\xd1\x01\x056\x14\x00 \x08\x0f(\x00@\x10\x03P\xa0L\x018H\x99n\xa8eD\x01\x00bd\xa21\xcc2\x05\x00H\x99n\xa8eD\x01\x00bd\xa21\xcc2\x05\x00H\x99n\xa8eD\x01\x00bd\xa21\xcc2\x05\x00H\x99n\xa8eD\x01\x00bd\xa21\xcc2\x05\x00H\x99n\xd5j\xfd\xf3\xf5\xbfO[\x8d\xfd}\xfcy\xac\xd6\x19\x1a\xcaV\x00\x80dKVVa\x02\xc1\x0f\xc3\xfd\xd8\xc2\xb0\t\xc6u/\xfe\xe8\xfd\xf0;\xfc\xff\xab\xbb;\x02\x9c\xb2y\xc8\xad\x05@r\x15K,\xff\x1e\x88\\\x18\x12;q#4\x7f\x1e\x1f~\xa4\xd6@\xb9<\x05\x00H\x9e^\xd1\xd2\x01\x8c\xd1%\xa8\xa0\xb8u\t\x80%:9\x05\x05\x00H\x81h\xcb*\xed\xa0X\xbfx\xef\xdd\x01\xaeRab\x9ds\x00d\x87\x8e\xd2\xc0X\x0e%\x80\x82\xfd\xca\x8e\t\x06 \xe5\xe2\xfd\xfb\xf5\xdb\x8fapo\x1b\xee\xf2v8j\xc2Q\xcaU\x86\x83dj\xa7\t\x8c5GA\xea\x957\xe1\x00$C\xaf\x0f_\xbe?\xf3o\xbe3.0\xa1(\xdc$A\xa4Y\x11\x00\x92\xa0\xd7\xb8\xd7x}N(\xaa\xa6\x08@I\x9b*\x00\x12\xd1IsJ\x15\x0b\x01@\x12S\x08\xa7X\x9b\n\xf5\x0c\xc74p@\xb2\r\t\x1c\xe4\x86>=\xec7\xe2\xeb\xe3\x19\x93\xe3\xcb\xd3\xaf\xcf\xe9\xe5\xed\x94\x04 +sm\x0b\x0e@\xb2\x85;\x00Y\xa8c\x13\x0e@r\x0b\x12\x002S\xc6\xc2\x9e#\x9e\x1cy\xa4[8\xe6\xbd\x0e\x13\xc0q\xd1\x04\x1b\xf7\x99\x16\xf1\x15\xa5\xff\x12\x80\xe3z\x8e\x01\xc9\xa8\x89\xf9\x14\xab\xc7\x9b\x80\xb5\x96\xb4\xc1\xdf}\xb6\xfeb\x96y@lo\xcac(a?b\x1a\x10\xa4V1@\x9c\xb3\x9ej\x99\x06\xe4\xc3\x97oC<D\xa8K\xf8\xf3G\x19\xa6w\xceC\x8f\xc3\xe0?\x8e=s\xbf\x99x=^\xcb\xa9\x96Y@\xda\xb9\xc7\x08\xc4\xe0\xfd!5\xbf\x0f\xd7:B\xd3\xea\xfd\x13\xbb\xa9\x96I@\xda\xc0\xe1\x8f9P\xdc\xf2\xadV\xb0Xu\x11\x93\x80\xf0\xa6Vu\xc0X\x02\xc3\x0f\x8aM\x171\x07\x08\xa7{plp9\xc7c\xd1E\x00\x08\xd1\x1e\x9c3\x98\xf8 \xb1\xe7"\xa6\x00\xe1\t$\x9a\x94*\xc61\xd7\x17V8\xc1\x8f\x8d\x99\xe3\xef\x00\xa4\xb2\xca/O\x0f\xcd4\xe5y*\xc0\x96\x8b4\x9b\xcc\xcaq\x99\xd4\x1c\xf5\xe6\x9cc\xcf\x11\x1b(\x07$-\x17\x81\xd8\xf8k\xff\xdd\x0c \xd4\xe9\x95\x048\xa6\xe0\xa0\x1e\xab\xa54\x0b\x80TXr$\xc11\r\x87\xf6\x193;i\x96\x19@(\xd3+\x89)\x07u\xaa%q\xcc\x15\xd6\xba\xab&L\x00B\x19,\x12\xdd\x83\xc3E\xac\xa4Y&\x00\xa1\xcc\xc9%\xaf\xa4V\x17\x86\x9aNb\x02\x10\xaa|\\\xb2{\xd0\xbb\x88\x8d}\x88\x11@h\x1ek\xd7\x00\x08\xa5\x8bHv\xcfZ.\x02@v(\xa9%@\xa8\x0e(\xb4\x8c\x7f\xc7\x14\xf7\xffN:\xdd\n\xaa\'\xc5\xa0J1-l\xd4\xbbw\x10\xaa\r\xba\x86\xf4\x8a\xfa\xc6!\x00\xd9\xe3MB\xea\x02\x10\xe7\xa8\\T\xd3"Q\x1a\x8ep\x90B\xe54\x05\x07\x00)\x9cd\x0b\xdf\xc5\xa2r\x10M\xe9\x05\x15 \xce\xe9\xd9\x87\x95"\x02\x07)T\x0e\x80\x04\xe1\x00Ha\xf8\xc8\xa9\x06\x07\xc1\x1edO4\xc2A\n\xd5\xd3\xe4 T\x8b\x84\xa6}X\xe14\xe3>H\xb1p\xde\x1d\xb4\xfc\xa42\x00)\x9de\x03\x1f\xaf\xc6\x06\xd59*@4\xb9h)"\xdd\xa7X\x00\xc49\xaaGM\x00H)v\x82\xea\xd1\x01\x12>\x1f\xaa\xe3\xe7\x01\x00Hy@v\xef A\x1a\xcb\x01B\x95^\x05]\xf1\xb0b9x\xa2jR=\xac\xa7\xe1>\x00\x1d \xfd\xdf\x039\xdd\xe9\x11\x15\xc9D\x17C\x17$\xb2\xd3,\xcaq[8\xe25\x03\x08\xe5>D\xb2\x8b\x00\x90\xfd+\xae\t\x07\xa1\xdc\x87\x84\xb6%n\xd6)\xe1\xb0\xb2\xff0\xe3 # \xdf\x9f\xe9~\xadI^>Nu01\xae\xc9\xf2\xc6\xbb\xdf+\xd6[0\xe3 \xd4+\xaa\xa4\xa0\xa1\x1e\xab\x95\xfd\x87)\x07\xa1\xdd\x87\xbc\xad\xab\x02\x1e?\xa1\x86\xe3\x144\x02\xc6I\xe5\x18\xcbv\xcd8\x08}\x9a\xd5\x1e\x12\x0e8$9%\x07$\xa6\x00\xe1p\x91V+,\x0f\x1c\xb6\xdc\xc3T\x8a5\xad6\xb4\x9b\xf5\xcb\x9a\xc6\x99\x86p\xc1a\xe9\xf4j\x9aIS\x0e\x12\x06\xcd\xe5"\xd3iO\xf8\xeds\xaa\xc7\xe2\xb9~U\xea\x1c,\x86\xf6\x1ef\x01\xa1\xbe\'\xb2\x96\x17\xd7v\x13n0\xa61Yx\xf6\xca\xf4&\x9d;\xcd\xba\x12\xdb\xbb\xc3\xab\xbb;\xfe}\xfcy,\xd9`\xb6\x02\xa3\xd5\xbe\xaaD\xa3\xdau\xcc\xa5X\x17Hh\xbe\xd7\x9b:A\xc1UB\xd9-`\x02\x10\xa7\xe0\x1c\x86{\xba\x9b\x9ciWl\xd1=Ln\xd2\xa7p\xe0\xdd\x8b\xa4\x05\xa1\xd4R\xb5SD\xa9\xe3\\M\x8f5]l\xedk\xe5:\xd1\xaa}\xdd\x9c\xedY\x86\xc3\xb4\x83\xf0\x9fhq\x86u\xbd\xbe\xac\xa6V\xa6O\xb1\xe6\xe1\xc3y\x0f\xa1^\xd8\xf2\xb4d\xdd=\xcc;H\xebS-\x9e0/\xed\xc5\xce\x13\xbb[\n\x99=\xc5Z\x8a\x82\xfd\xc8{E\xac\xa7VH\xb1\x16\x84\xe0T\xeb"\x88\xc4\x17\xc0J}po=8\xc8LA@"\xf3\xed\xc8\xbdA\xbe\xa7>\x00\x81\x93\x9c\x15\x80s\\\xa3\x04@V\x96\x17\x8bN\x82\x13\xabu\x9f\x01 7\xfc\xd7\xd2\xf1/\xe0\xb8\x9d\x84\x01\x90\x8d\x04\xb5\xe5\xc3\x81{\xf2\xe6\xf4\xba\xfe8x\x7f(}x2\xbd\x1f\xbd%\x01H\xc2\xdc\xf5\xe9&\xb8\xcf\x910\xf56\xbe\xac\x98"D\xacLO\x90 \xa5\x8a\xcd\xf6\xe5\xefp\x90t\xad\x98\xdfF\xcc\xb8\xb0\x8c\xa28\xa9\xca\x10\xcb\xca\xb7y\xf3$\x89\x97\xd6\xe8&p\x8d\xf8\xbc\xae\x95\x80\x83\x94\xe9v\xaa\xa5\x01\x14\x80\xb1c\x82\xe1 \xfb\xc4\x9bj\xcb\x04\x05\'T5f\x17\x0eRC\xc5\xb76\xda\x83\xe2O\xef\xba\xe3\xe8\xb6\xde\xa4\x02\x90zZ\x9e[\n\xf7O\xee\xdc\xeb\xa7ap\xf7\x04\xcd/\x9a\x04\x14\x94\x1a\x03\x10Ju\x89\xbf\xc3\x85\x13)\xe2\xc9\xc3\x1e\x84^\xe0\xd0\x03\xd5O\x11\xe0\x9d\r\xfa\xf9\x83\x83\xd0k\x0c@\x184\xa6\xea\x02\x80P);k\x17\x0e\xc2 2Q\x17\x00\x84H\xd8y\xb3\x00\x84Ad\xa2.\x00\x08\x91\xb0\x00\x84AX\x86.\x00\x08\x83\xc8p\x10\x06\x91\x89\xba\x00 D\xc2\xc2A\x18\x84e\xe8\x02\x800\x88\x0c\x07a\x10\x99\xa8\x0b\x00B$,\x1c\x84AX\x86.\x00\x08\x83\xc8p\x10\x06\x91\x89\xba\x00 D\xc2\xc2A\x18\x84e\xe8\x02\x800\x88\x0c\x07a\x10\x99\xa8\x0b\x00B$,\x1c\x84AX\x86.\x00\x08\x83\xc8p\x10\x06\x91\x89\xba\x00 D\xc2\xc2A\x18\x84e\xe8\x02\x800\x88\x0c\x07a\x10\x99\xa8\x0b\x00B$,\x1c\x84AX\x86.\x00\x08\x83\xc8p\x10\x06\x91\x89\xba\x00 D\xc2\xc2A\x18\x84e\xe8\x02\x800\x88\x0c\x07a\x10\x99\xa8\x0b\x00B$,\x1c\x84AX\x86.\x00\x08\x83\xc8p\x10\x06\x91\x89\xba(\x02$|\xf7\x89\xe8z\xaa7+\xe1\xb7/z\x06\xa4\xf7X\xc8\x06D\xd3\xcf\x93I\xf9.m\xcf\x80\xb4\xff\x9ad\xfa\x9aZ\xf2\x1d\xb1n\x01\x91\x02G\x98\xbe\x9e\x01\t\xe3\xd3\x02\t\x00y[L$\xc1a\x01\x10-\x90\x00\x90\xf0\xa9H\xef\x0e\x7f\x1e\x1f~\xa4\x1b/}\xc9\xde\x1ddRP\xba\x93\x98\x07D"\x1cV\x1cD\x03$\xa6\x01\x91\n\x875@$\xa7[f\x01\x91\x0c\x87E@\xa4Bb\x12\x10\xe9pX\x05D"$\xe6\x00\xd1\x00\x87e@\xa4Ab\n\x10-pX\x07D\x12$f\x00\xd1\x04\x07\x00\x19\xcf\xb7$\x1c\x01\x9b\x00D\x1b\x1c\x00\xe4r\x9f\xe9\xc3\x97\xef\xcf\xce\r\xcd\x9e\xe33\x01\x88s\xfe\xf8\xf2\xf4\xeb3\xfd\xed\xbdz=X\xb9Q\x18S\x0c\x80\xc4\x14\xaa\xf4wm.\x02@\x90bU\n\xfd\xf4fJ\xec2\xbd\xf5\xba%\xad\x03"\xe5\t\xf0\x92\x98Q\xfc4\xaf\x9eT\xcb: \xadS\xabi\xb93\x06\x88\xcc\x07\x13\xd7\xbc\xc72 \x12N\xaf\xcc\x02\x12\x06^\xb2*\xd4M\xa0\xe2\xadY\x05DJje\x1a\x10\r\x90X\x05\x84j\xdc\xf1%i\xbdD\xc9b\xaax\x0f2\x17A\xf6~\x84*P^\x9e\x1e\xb2\xe7\xaf4\xb8r\xebI\xd9w\xcc\xaf\xdb0 A\x06\xb9\x90X\x03D\xd2\xbe\x03\x80\xcc\x14\x90z\x7f\xc4\x12 R\xe1(M\xc5\xb3-Z\xda\xc6ki\xfd\x12!\xb1\x02\x88d8\x00\x88`\'\xb1\x00\x88t8\x00\xc8\xc2J$9I\xef\x80h\x80\x03\x80\xac\x1c\xb3H\x81\xa4g@\xb4\xc0\x01@n\x9cCJ\x80\xa4W@4\xc1\x01@6\x0e\xea[C\xd2# \xda\xe0\x00 \xd1;Y\xed\xee\x93\xf4\x06\x88\xc4\x9b\x80\xd1\xe9/|,\xa9\xbbc\xde\x98P-\xdc\xa4\x17@\xa4\x1f\xf1\xc7\xe6^\xec\x9d\xf4\x10\x94\'\x8b\x1b\xdc}l\x10\x1c\x7f\xe7\x86\xa4\x07@$\xa5T\xa5\xf1$\x12\x90y0J\xb2fNH\xb4\x03"i\xde\xe6\x8f\x14\xe5B+\x0e\x90\xb5 \x94%6\xcf;%Z\x01\x19S\xaa\xe1\xbe\xe5\x87\x16\x96\x19\xc5\xf2\x01\xcd\x1cHD\x01rk\x85\x96\x98\xc7R\xbb\x896@$\x82\xb1u\n\x95\n\x89\x18@b\x01\'\x11\x92\xd3\xf3\xc0D?\x9d\xa0\t\x90\xd4`\xe3\xd8+\xbe{\xa1!27)\xd7-\x02\x90\xd4 K\x19\x10\xf7$L\xfd\xa5\x8e!\xf5\xfa4\x00"\xd55r\x16\xaeXL5\x07$7\xb0b\x03J\r@\xaar\xb9\xe3\xb9u\x1d\x92\x01\x91\x0cF\x0e\x1c\x93\xf6[1\xd5\x14\x90\xd2`\x92\xb6i_\x0b\xf2\xd2\xb1MmI\x04D:\x18\xa3ve7woA\xd2\x0c\x90\xbd\x01$\xddI\xf6\xa6^R\x00\tP\xdc\xb9\xd7OR\xeeGm;\x7f\x19\x1c[N\xd2\x04\x90\xbdp\xa4X#U\nU\xde\xae?z?\xfcN\xfd-\xc4\x96\x80L\xbfc.\xed\xb8vK{\xaa\x98b\x07\xa4\xd6@tBr\xf6\x95(,-\x00\xd1\x91B]cB\x19S\xac\x80\xd4\x1e\x88nH.\x13==\x06\xf1\xea\xee\x8e\x7f\x1f\x7f\x1e\xc3_\xa8\x01y\xef\x12\xa7;\x06\xcd\xbe\xa0^\xee\xcat\xc7\xecS\n\xcf\x06H\xc8cS\xd3\x8b\x12\xc1\xb4\xecI\xd2\xc6\xe6\x8ft\x01K\xd9v\xda\xe8j\x95\xa2Zp\xe7\x0b\xef|\xd1J\xbd\xee\xec\xa7yS\x1b\xde[\xae/H\xf6\xaa\xd1w}j8\xf6\xa8\'\x16\x900(\xa9w\xdc\xf7\x08\x8e\xba\xef\x15(I{85\x14\r\xc8$\x84\x86{%\x9c\x93\xd6G_\xfe8x\x7f\x98\xf6iR\xc7\xa4\x02\x90 \x1eR.\xa9!\x94\x7f]\x92S\xaa\xe5h\xd4\x00\x02H\xf2\x03Qb\r\xe9)\x95j@\xe6\'\x12:\xee\x06K\x0c\xd1V\xd7\xb4\xef\xcex\xb3\xabn\xd5\xf1\xde~\x91r\xedU\x90\xaf\xbe\xa6\x94\xaa\x0b\x07\x99\x0f\x02\x1bx\xbe@\xcf\xefI\xc7F|k\\\xaa\xf6 \xb7\x06\x027\xc9\x0f]\xea\x1a\xda\xf6\x1a\xb7\xf4\xe8\x02\x10\xecM\xa8\xc3=\xbd}\xcd\xe9\xd4\xda(\xbb\x02\x04\xa0\xa4\x07r\xfd\x92:7\xe11\x1d\xba\x04\x04\xa0\xc4\xa6\xbd\xe6\xdf\xf5\xef3\xba\xdf\x83l\r0\xecO\xc2\xdfq,\\\x13\x8a\xd0V\xdf`Lju\xed \xf3\x90\x00(\xb5\x00\xb1\x01\x869@\x96\xb0\xc0Qr\x80\x19\xdf\xa0,y\\<\xa7\x17\x89e\xcd8\xc8\x9a\xf8p\x95XH\xdar\x0b3\xa7X\xb1i\xbf\x05\x0b\\\xe5\x9cX\xa8x\xd2\xb6d\x9es\xeb\x98v\x905\xb1._\xfe\xf0\x1f\xe9\xde\x04\xcc\x9d&\xea\xf2\xe1\xcdD\xe74<~N\xad\xc4\xb2}\x00\x12Q\xbc\xdf4lL\x9f\xc2\xf0\xa5\xbf\x93\xc1\r\xc5\xbc?\x00\x92\xa1\xbenw\x81KdL\xf5\xb9(\x00)Q\xed\xad\xce\x04\xcc)=\x19\xa4\xa4d#\x08\xd3\xa9\x13\x1cb\xc7\x04\x07\x1d\xf7UG\xed\xad}\xcc\xf4\xb7\x11\x9e\x13F\x15>\xc73\x020\xfd\x03\x08\xb41\x08@h\xf5Mj}\xfa\xae\xd5\xb20\xf6\x06I\xf2\x91\x16\x02 \xa4\xf2\xa2q\xed\n\x00\x10\xed3\x88\xeb\'U\x00\x80\x90\xca\x8b\xc6\xb5+\x00@\xb4\xcf \xae\x9fT\x01\x00B*/\x1a\xd7\xae\x00\x00\xd1>\x83\xb8~R\x05\x00\x08\xa9\xbch\\\xbb\x02\x00D\xfb\x0c\xe2\xfaI\x15\x00 \xa4\xf2\xa2q\xed\n\x00\x10\xed3\x88\xeb\'U\x00\x80\x90\xca\x8b\xc6\xb5+\x00@\xb4\xcf \xae\x9fT\x81\xff\x01i\xaa\x9aA\x89@\xd8b\x00\x00\x00\x00IEND\xaeB`\x82'
icon_id = idaapi.load_custom_icon(data=icon, format="png")

class Utils:    
    def get_func_name(ea):
        # Get pretty function name
        func_name = Utils.get_pretty_func_name(idc.get_func_name(ea))
        if not func_name:
            func_name = Utils.get_pretty_func_name(idc.get_name(ea))
        return func_name

    def get_pretty_func_name(name):
        # Demangle function name
        demangled_name = idc.demangle_name(name, idc.get_inf_attr(idc.INF_SHORT_DN))
        # Return as is if failed to demangle
        if not demangled_name:
            return name
        # Cut arguments
        return demangled_name[:demangled_name.find("(")]
    
    def prep_func_name(name):
        if name[0] != "." and name[0] != "_":
            # Name does not start with dot or underscore
            return [name,f".{name}",f"_{name}"]
        else:
            return [name[1:],f".{name[1:]}",f"_{name[1:]}"]

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.all_nodes = set()
    
    def add_edge(self, u, v):
        self.all_nodes.add(u)
        self.all_nodes.add(v)
        self.graph[u].append(v)

    def is_path_exists(self, source, target, visited=None):
        if visited is None:
            visited = set()
        if source == target:
            return True
        visited.add(source)
        for neighbor in self.graph[source]:
            if neighbor not in visited:
                if self.is_path_exists(neighbor, target, visited):
                    return True
        return False

    def is_node_exists(self, node):
        return node in self.all_nodes
    
    def get_neighbors(self, node):
        return self.graph[node]
    
    def get_all_nodes(self):
        return list(self.all_nodes)


class LibraryAnalyzer():
    def __init__(self):
        self.bin_path = None
        self.rootfs_path = None
        self.libraries_graph = None

    def init_analyzer(self, bin_path, rootfs_path):
        self.bin_path = bin_path
        self.rootfs_path = rootfs_path
        self.libraries_graph = Graph()
        
        self.generate_libraries_graph()

    def get_needed_libraries(self, bin_path):
        # parse .dynamic section of the binary
        needed_libraries = []
        with open(bin_path, 'rb') as f:
            elffile = ELFFile(f)
            for segment in elffile.iter_segments():
                if segment.header.p_type == 'PT_DYNAMIC':
                    dynamic_segment = segment
                    break
            if not dynamic_segment:
                print("%s: No dynamic segment found" % bin_path)
                return []
            for tag in dynamic_segment.iter_tags():
                if tag.entry.d_tag == 'DT_NEEDED':
                    library_name = elffile.get_section_by_name('.dynstr').get_string(tag.entry.d_val)
                    if library_name not in needed_libraries:
                        library_path = self.locate_bin_in_rootfs(library_name)
                        # print("%s: depends on %s" % (bin_path, library_path))
                        needed_libraries.append(library_path)

        return needed_libraries
    
    def generate_libraries_graph(self):
        queue = deque()
        visited = set()
        queue.append(self.bin_path)

        while queue:
            current_bin_path = queue.popleft()
            if current_bin_path in visited:
                continue
            visited.add(current_bin_path)
            needed_libraries = self.get_needed_libraries(current_bin_path)
            for library_path in needed_libraries:
                self.libraries_graph.add_edge(current_bin_path, library_path)
                # print("Adding edge: %s -> %s" % (current_bin_path, library_path))
                if library_path not in visited:
                    queue.append(library_path)
                
        
        # print("Graph: %s" % self.libraries_graph.graph)
        # print("All nodes: %s" % self.libraries_graph.get_all_nodes())

    def locate_bin_in_rootfs(self, bin_name):
        result_path = None
        for dirpath, dirnames, filenames in os.walk(self.rootfs_path):
            if bin_name in filenames:
                bin_path = os.path.join(dirpath, bin_name)
                if os.path.islink(bin_path):
                    real_path = os.path.realpath(bin_path)
                    if os.path.exists(real_path):
                        return real_path
                    # else:
                    #     print("Symbolic link %s points to non-exist file" % bin_path)
                else:
                    result_path = bin_path
        if result_path:
            return result_path
        # print("[!] %s not found in rootfs" % bin_name)
        return None
                    

class FunctionAnalyzer():
    def __init__(self):
        self.bins_graph = None
        self.exported_functions = None

    def init_analyzer(self, bins_graph):
        self.bins_graph = bins_graph
        self.exported_functions = defaultdict(list)
        
        self.init_exported_functions(bins_graph)
    
    def init_exported_functions(self, bin_path):
        for bin_path in self.bins_graph.get_all_nodes():
            if bin_path not in self.exported_functions:
                self.exported_functions[bin_path] = []

            with open(bin_path, 'rb') as f:
                elffile = ELFFile(f)
                # find .dynsym section and parse it
                for section in elffile.iter_sections():
                    if section.name == '.dynsym':
                        for sym in section.iter_symbols():
                            if sym.entry.st_info['type'] == 'STT_FUNC'  and sym.entry['st_shndx'] != 'SHN_UNDEF':
                                self.exported_functions[bin_path].append(sym.name)
        # print(self.exported_functions)

    def locate_function_in_bin(self, function_name):
        if not self.exported_functions:
            print("No exported functions found in any binary")
            return None
        for bin_path, functions in self.exported_functions.items():
            for func in functions:
                if function_name in Utils.prep_func_name(func):
                    print("Function: %s -> %s" % (function_name, bin_path))
                    return bin_path
        print("Function: %s not found in any binary" % function_name)
        return None

class Locator():
    def __init__(self):
        self.libraries_analyzer = LibraryAnalyzer()
        self.functions_analyzer = FunctionAnalyzer()
        self.rootfs_path = None
        self.bin_path = None

    def init_libraries_analyzer(self, bin_path, rootfs_path):
        self.rootfs_path = rootfs_path
        self.bin_path = bin_path
        self.libraries_analyzer.init_analyzer(bin_path, rootfs_path)

    def init_functions_analyzer(self, bins_graph):
        self.functions_analyzer.init_analyzer(bins_graph)

class LocatorHandler(idaapi.action_handler_t):
    def __init__(self, function_name):
        idaapi.action_handler_t.__init__(self)
        self.function_name = function_name

    def activate(self, ctx):
        global locator
        # print(locator.libraries_analyzer.libraries_graph.graph)
        # print(locator.functions_analyzer.exported_functions)

        if locator.rootfs_path is None:
            ida_kernwin.warning("Please init plugin: input the rootfs path \nEdit -> Plugins -> Function Locator")
            return 0

        target_bin_path = locator.functions_analyzer.locate_function_in_bin(self.function_name)
        if not target_bin_path:
            ida_kernwin.warning("Function: %s not found in any binary" % self.function_name)
            return 0
        target_bin_relative_path = os.path.relpath(target_bin_path, locator.rootfs_path)
        ida_kernwin.info("Function: %s -> %s" % (self.function_name, target_bin_relative_path))        

        return 1

    def update(self, ctx):
        return idaapi.AST_ENABLE_ALWAYS

class Hooks(idaapi.UI_Hooks):
    def __init__(self):
        idaapi.UI_Hooks.__init__(self)

    def finish_populating_widget_popup(self, form, popup):
        function_ea = idc.here()
        function_name = Utils.get_func_name(function_ea)

        action_text = f"Locate '{function_name}' in rootfs"
        try:
            # Get selected symbol
            selected_symbol, _ = ida_kernwin.get_highlight(ida_kernwin.get_current_viewer())
            # Check if it is a function name
            for function in idautils.Functions():
                if Utils.get_func_name(function) in Utils.prep_func_name(selected_symbol):
                    action_text = f"Locate '{Utils.get_func_name(function)}' in rootfs"
                    function_name = Utils.get_func_name(function)
        except:
            pass
        action_desc = idaapi.action_desc_t(
            'Function Locator',   # The action name. This acts like an ID and must be unique
            action_text,    # The action text.
            LocatorHandler(function_name),       # The action handler.
            '',             # Optional: the action shortcut
            'locate the library that contains the function in the rootfs',  # Optional: the action tooltip (available in menus/toolbar)
            icon_id         # Optional: the action icon (shows when in menus/toolbars)
        )
        idaapi.unregister_action("Function Locator")
        idaapi.register_action(action_desc)
        if ida_kernwin.get_widget_type(form) == idaapi.BWN_DISASM or ida_kernwin.get_widget_type(form) == idaapi.BWN_PSEUDOCODE:
            idaapi.attach_action_to_popup(form, popup, "Function Locator", "")


class FunctionLocatorPlugin(idaapi.plugin_t):
    flags = idaapi.PLUGIN_UNL
    comment = "Function Locator"
    help = "a plugin hels IOT Security Researchers to locate the library that contains the function in the rootfs"
    wanted_name = "Function Locator"
    wanted_hotkey = "Alt-F"

    def init(self):
        self.rootfs_path = None
        self.bin_path = None
        return idaapi.PLUGIN_OK

    def run(self, arg):
        global locator
        importlib.reload(function_locator)
        self.bin_path = ida_nalt.get_input_file_path()
        self.rootfs_path = ida_kernwin.ask_str("", 0, "Enter the path to the rootfs")
        if not self.rootfs_path or not os.path.exists(self.rootfs_path) or not os.path.isdir(self.rootfs_path):
            ida_kernwin.warning("Invalid rootfs path")
            return
        
        locator.init_libraries_analyzer(self.bin_path, self.rootfs_path)
        bins_graph = locator.libraries_analyzer.libraries_graph
        locator.init_functions_analyzer(bins_graph)
            
    def term(self):
        pass

hooks = Hooks()
hooks.hook()
locator = Locator()

def PLUGIN_ENTRY():
    return FunctionLocatorPlugin()