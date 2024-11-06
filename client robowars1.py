import socket
import json

def get_motor_values(f, b) -> tuple:
    print(f"The motor inputs are given as {f}, {b}")
    return f, b  # sample motor left and motor right PWM values.

def main(ip_addr, port) -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip_addr, port))

    try:
        
        while True:
            
            received_data = client_socket.recv(1024).decode().strip()
            print(received_data)
            print(f"Received data from server: {received_data}")

            if not received_data:
                continue
            received_data=json.loads(received_data)

            if received_data['s3'] == 1:
                s='motor "f" "50" "f" "50"\n'
                res = s.encode('ascii')
                client_socket.send(res)
                print('Sent data ',res)

            else:
                if received_data['s1'] == 1:
                    print('s1 is returning 1')
                    s='motor "f" "40" "f" "60"\n'
                    res = s.encode('ascii')
                    client_socket.send(res)
                    print('Sent data ',res)

                elif received_data['s2'] == 1:
                    print('s2 is returning 1')
                    s='motor "f" "40" "f" "55"\n'
                    res = s.encode('ascii')
                    client_socket.send(res)
                    print('Sent data ',res)

                elif received_data['s5'] == 1:
                    print('s5 is returning 1')
                    s='motor "f" "60" "f" "40"\n'
                    res = s.encode('ascii')
                    client_socket.send(res)
                    print('Sent data ',res)

                elif received_data['s4'] == 1:
                    print('s4 is returning 1')
                    s='motor "f" "55" "f" "40"\n'
                    res = s.encode('ascii')
                    client_socket.send(res)
                    print('Sent data ',res)
                
                elif received_data=={'s1': 0, 's2': 0, 's3': 0, 's4': 0, 's5': 0}:
                    print('All sensors are returning 0')
                    s='motor "b" "40" "b" "40"\n'
                    res = s.encode('ascii')
                    client_socket.send(res)
                    print('Sent data ',res)

            
    except Exception as e:
        print(e)

    finally:
        client_socket.close()

#if __name__ == '__main__':
    #main('127.0.0.1', 12345) 
