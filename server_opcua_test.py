import sys
sys.path.insert(0, "..")
import time
from Xlib import display
from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")


    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    myobj = objects.add_object(idx, "MyObject")
    #myimg = Image.open("./track_cm.png")
    #img = myobj.add_variable(idx,"myimg",myimg)
    mystr = myobj.add_variable(idx, "MyString", 6.7)
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    x=myobj.add_variable(idx,"X",0)
    y=myobj.add_variable(idx,"Y",0)
    myvar.set_writable()    # Set MyVariable to be writable by clients
    x.set_writable() 
    y.set_writable() 
    # starting!
    server.start()
    
    try:
        mystr.set_value("Hello There")
        count = 0
        while True:
            #time.sleep(1)
            data = display.Display().screen().root.query_pointer()._data 
            x.set_value(data["root_x"]), y.set_value(data["root_y"])
            
            #count += 1
            #myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()
