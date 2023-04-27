Algoritma Breadh-First Search menggunakan library pygame

Breath-First Search (BFS) adalah sebuah algoritma pencarian graf yang melintasi simpul-simpul secara melebar, mulai dari simpul awal, dan menelusuri semua simpul yang terhubung ke simpul awal tersebut, lalu menelusuri simpul-simpul tersebut secara sistematis dan berurutan. Algoritma BFS berfungsi dengan mengunjungi setiap simpul dalam graf tepat satu kali.

Proses BFS dimulai dari simpul awal, lalu mengekspansi simpul tersebut dan menelusuri semua simpul yang terhubung langsung ke simpul tersebut. Kemudian, proses ini dilanjutkan dengan menelusuri simpul-simpul yang terhubung ke simpul-simpul yang telah dikunjungi sebelumnya, tetapi belum pernah dikunjungi sebelumnya.

Algoritma BFS biasanya diimplementasikan dengan menggunakan antrian (queue). Saat proses BFS dimulai, simpul awal dimasukkan ke dalam antrian. Kemudian, simpul ini dihapus dari antrian, dan simpul-simpul yang terhubung langsung dengan simpul awal dimasukkan ke dalam antrian. Selanjutnya, simpul-simpul ini dihapus dari antrian satu per satu, dan simpul-simpul yang terhubung langsung dengan simpul-simpul ini dimasukkan ke dalam antrian, dan seterusnya. Proses ini berlanjut hingga seluruh simpul yang terhubung dengan simpul awal telah dikunjungi.

Algoritma BFS sering digunakan untuk mencari jalur terpendek antara dua simpul dalam graf. Selain itu, algoritma BFS juga dapat digunakan untuk menghitung jarak terpendek dari simpul awal ke simpul yang lain dalam graf, serta untuk menemukan semua simpul yang dapat dicapai dari simpul awal.
