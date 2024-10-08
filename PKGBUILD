pkgname=mutercim  
pkgver=1.0.0      
pkgrel=1          
arch=('any')      
pkgdesc="An instant translation application"  
url="https://github.com/aspidisu/mutercim"  
license=('MIT')  
depends=('python' 'python-requests' 'tk' 'python-pyqt5')  
source=("mutercim.py" "install.sh" "translation.png" "mutercim.desktop")  
md5sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')  

package() {
    mkdir -p "$pkgdir/usr/bin"  
    install -Dm755 "$srcdir/mutercim.py" "$pkgdir/usr/bin/mutercim" 
    install -Dm755 "$srcdir/install.sh" "$pkgdir/usr/bin/install-mutercim"  
    install -Dm644 "$srcdir/translation.png" "$pkgdir/usr/share/icons/hicolor/256x256/apps/translation.png"
    install -Dm644 "$srcdir/mutercim.desktop" "$pkgdir/usr/share/applications/mutercim.desktop"
}
