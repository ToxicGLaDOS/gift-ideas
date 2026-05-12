#!/usr/bin/env python3

import csv

class Game:
    def __init__(self, platform, title, country, publisher, developer, price_cib):
        self.platform = platform
        self.title = title
        self.country = country
        self.publisher = publisher
        self.developer = developer
        self.price_cib = price_cib

with open('gameWishlist.html', 'w') as wishlist_out:
    with open('gameye_wishlist_current.csv') as wishlist:
        wishlist_out.write('<head>')
        wishlist_out.write('<link rel="stylesheet" href="/static/table.css">')
        wishlist_out.write('</head>')

        reader = csv.DictReader(wishlist)
        wishlist_out.write("<table>")


        wishlist_out.write('<tr>')
        wishlist_out.write('<th>Platform</th>')
        wishlist_out.write('<th>Title</th>')
        wishlist_out.write('<th>Release Country</th>')
        wishlist_out.write('<th>Publisher</th>')
        wishlist_out.write('<th>Developer</th>')
        wishlist_out.write('<th>Approx. Price CIB</th>')
        wishlist_out.write('</tr>')
        for row in reader:
            game = Game(row['Platform'], row['Title'], row['Country'], row['Publisher'], row['Developer'], row['PriceCIB'])

            wishlist_out.write('<tr>')
            wishlist_out.write(f'<td>{game.platform}</td>')
            wishlist_out.write(f'<td>{game.title}</td>')
            wishlist_out.write(f'<td>{game.country}</td>')
            wishlist_out.write(f'<td>{game.publisher}</td>')
            wishlist_out.write(f'<td>{game.developer}</td>')
            wishlist_out.write(f'<td>${game.price_cib}</td>')
            wishlist_out.write('</tr>')

        wishlist_out.write("</table>")
