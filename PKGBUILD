# Maintainer: Senin Adın <senin.email@example.com>
pkgname=mutercim
pkgver=1.0
pkgrel=1
pkgdesc="Kopyalanan metni otomatik olarak çeviren bir Python uygulaması."
arch=('x86_64')
url="https://yourprojecturl.com"
license=('MIT')
depends=('python-requests' 'python-pyperclip' 'tk')  # python-tk yerine tk
source=('mutercim.py' 'requirements.txt')
md5sums=('SKIP' 'SKIP')

package() {
    install -Dm755 "$srcdir/mutercim.py" "$pkgdir/usr/bin/mutercim"
    install -Dm644 "$srcdir/requirements.txt" "$pkgdir/usr/share/doc/$pkgname/requirements.txt"
}
