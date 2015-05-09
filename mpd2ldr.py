import sys, re
args = sys.argv[1:]

def get_source ( file_path ):
    f = open( file_path, "r" )
    s = f.read()
    return s
    
def identify_parts () :
    pass

def get_extension( file_path ):
    ext = i.split(".")[-1:]
    return ext[0]    

def get_modules( source ):
    header_regex = "(0 FILE[^\n]*)";
    sub_modules = re.split( header_regex , source )
    return modules
    
for i in args:
    if ( get_extension(i).lower() == "mpd" ):
        s = get_source(i)
        for i in get_modules ( s ):
            print ( i )
            print ( " --- " )
            
    else:
        print( "Error: '" + i + "' is NOT an MDP file." );
