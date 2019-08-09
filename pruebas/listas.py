def listas():
    lista = ['manzana', 'uva', 'pera']

    print(lista.__contains__('aguacate'))
    print(lista.index('aguacate'))

def discoDuro():
    import sys
    import os
    import fcntl
    import struct

    if os.geteuid() > 0:
        print("ERROR: Tienes que ser root")
        sys.exit(1)

    with open(sys.argv[1], "rb") as fd:
        hd_driveid_format_str = "@ 10H 20s 3H 8s 40s 2B H 2B H 4B 6H 2B I 36H I Q 152H"
        HDIO_GET_IDENTITY = 0x030d
        sizeof_hd_driveid = struct.calcsize(hd_driveid_format_str)

        assert sizeof_hd_driveid == 512

        buf = fcntl.ioctl(fd, HDIO_GET_IDENTITY, " " * sizeof_hd_driveid)
        fields = struct.unpack(hd_driveid_format_str, buf)
        serial_no = fields[10].strip()
        model = fields[15].strip()
        print("Modelo del disco: %s" % model)
        print(" Numero de serie: %s" % serial_no)

discoDuro()