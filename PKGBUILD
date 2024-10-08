pkgname=mütercim
pkgver=1.0
pkgrel=1
pkgdesc="An instant translation application"
arch=('any')
url="https://github.com/aspidisu/mütercim"
license=('MIT')  # veya uygun bir lisans
depends=('python' 'python-requests' 'tk')
source=("mütercim.py" "install.sh" "translation.png" "mutercim.desktop")
md5sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 "${srcdir}/mütercim.py" "${pkgdir}/usr/bin/mütercim"
    install -Dm755 "${srcdir}/install.sh" "${pkgdir}/usr/bin/install-mütercim"
    install -Dm644 "${srcdir}/translation.png" "${pkgdir}/usr/share/pixmaps/translation.png"
    install -Dm644 "${srcdir}/mutercim.desktop" "${pkgdir}/usr/share/applications/mutercim.desktop"
}
