### Basic-Network-Tools

#### Portscanner
<i>Portscanner.py</i> is a tool created to scan a specific port on a specific host.
Usage is from prompt:
```
python portscanner.py -H localhost -p 54321
Connecting to 127.0.0.1...
[FAILED] TCP port 54321 is closed
``` 
or `[OK] TCP port 54321 is open` 
if port is open.
#### Server and client

<i>server.py</i> and <i>client.py</i> are a pair of scripts that connect each other, echo-ing data.
Those are simple scripts, used for learning the basic usage of <b>socket</b> module.<br><br>
The server starts on a specific <b>host</b> and <b>port</b>, accepting one connection at a time.<br>
A good usage is to specify the <b>host</b> as an IPv4 address rather than a domain name (eg: 'example.com'). In this example
I used localhost, but you can use IPv4 address of inside network, or the external IP. If you would like to access from 
all addresses, (local machine, LAN, WAN), use empty string <code>''</code> as host.<br>
For <b>port</b>, is better to avoid numbers below 1024, because many of them are system reserved. A good usage would be a 4 or 
5-digit integer.<br><br>
What <i>server.py</i> script does is instantiating a socket object using the <code>socket()</code> function. The arguments for
socket() function are two constants: <i>AF_INET</i> and <i>SOCK_STREAM</i>. First one specifies the `AddressFamily`, in this case 
IPv4, and the second one `SocketKind`, the type of the socket - in this case, our socket is of stream type.<br>
Afterwards, the socket object binds to a specific host and port using `bind()` action, and starts listening on the specified port
`listen()` for a specific number of connections - in our case 1.<br>
When a client tries to connect to server, we say to our server to perform a new action - accept connection: `accept()`. Those are
the main actions that socket object needs to perform to act like a server.<br>
We declare a loop using `While True` to capture data received from client, using a specified buffer size - 1024 bytes.
Data is received in binary mode, so in order to print it to screen, we have to decode it using UTF-8 format.
Server sends back data, also in binary mode, prints to screen, and closes the connection.<br><br>
Meanwhile, <i>client.py</i> socket object has to perform only two actions: `socket()` and `connect()`. The arguments for socket and
connect are identical with `socket()` and `bind()` from server code.<br><br>

Let's take a look at each script output:<br>
`server.py` outputs:
```
Server started on localhost, listening on TCP port 54321
Incoming connection from 127.0.0.1:58666...
Received following data: Hello World!
Server is shutting down. Bye!
```
while `client.py` outputs:

```
Connected to server: localhost on port 54321
Sending some data...
Response from server: Hello World!
Connection closed.
```

Note that server does not communicates (`sendall()`,`recv()`) on the socket it is listening, instead uses the new socket
initiated with `accept()`.
