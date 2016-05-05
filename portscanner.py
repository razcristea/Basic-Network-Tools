import os.path
import sys
import socket
import argparse


def connection(host, port):
    try:
        host = socket.gethostbyname(host)
        socket_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = socket_conn.connect_ex((host, port))
        print('Connecting to {}...'.format(host))
        if response == 0:
            print("[OK] TCP port {} is open".format(port))
            socket_conn.close()
        else:
            print("[FAILED] TCP port {} is closed".format(port))
            socket_conn.close()
    except KeyboardInterrupt:
        print("Ctrl+C detected. Exiting...")
        sys.exit(1)
    except socket.gaierror as e:
        print("ERROR: {}. Couldn't resolve hostname".format(e))
        sys.exit(1)
    except socket.error as e:
        print("ERROR {}:Couldn't connect to server".format(e))
        sys.exit(1)


def Main():
    parser = argparse.ArgumentParser(
        description=">>>     Simple port scanner      <<<\n>>>  for specific host and port  <<<",
        usage="\n{} -H <target host> -p <target port>".format(os.path.basename(__file__))
    )
    parser.add_argument('-H', dest="host", type=str, help="IP of host to connect")
    parser.add_argument('-p', dest="port", type=int, help="PORT/PORTS to scan. Use comma to declare many")
    args = parser.parse_args()
    if not (args.host and args.port):
        print(parser.description)
        print(parser.usage)
        exit(0)
    connection(args.host, args.port)


if __name__ == '__main__':
    Main()
