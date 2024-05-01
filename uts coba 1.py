import socket

# Inisialisasi socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Binding ke alamat dan port tertentu
    server_address = ('localhost', 12345)  # Misalnya, menggunakan localhost dan port 12345
    server_socket.bind(server_address)

    # Mendengarkan koneksi masuk
    server_socket.listen(5)
    print("Menunggu koneksi...")

    while True:
        # Terima koneksi
        client_socket, client_address = server_socket.accept()

        with client_socket:
            print(f"Koneksi dari {client_address}")

            # Menerima data dari klien
            data = client_socket.recv(1024)
            print(f"Data yang diterima: {data.decode('utf-8')}")

            # Kirim balik pesan kepada klien
            response = "Pesan diterima, terima kasih!"
            client_socket.sendall(response.encode('utf-8'))
