# Short4SEO

Primitive CGI sctipt, which shortens URL via [bit.ly](http://bit.ly) service, allowing one to put not a direct link on site, but one "masked" with your domain

## What for ?
* You can cloak referral links to protect your earnings
* You can cloak links to another resources, to make sure your partners really want link - and not utilizing your web site as donor.
* You can simply mask ugly URLS.

## Installation
### Requirements
* Working web server with Perl CGI module
* WWW::Shorten::Bitly cpan module
* bit.ly account to get an API key

### How to install
*   Copy *.cgi to your cgi-bin directory
* Check permissions
* Modify url.cgi to match your username, API key and script location

## Usage
Open http://your.domain/cgi-bin/mkurl.cgi in browser and type-in full url (including this http://blablabla.com/lala/mumu/location, then click the button.

If everything is correctly set-up, you will get a link like
http://your.domain/cgi-bin/url.cgi?XxxYYY, which you can distribute or put into your content.

### url.cgi and rurl.cgi
* **url.cgi** just redirects to bit.ly with shorted url and target web-server. Finally, target web server gets a referal with your original page. E.g. if you placed shortened link somwhere on http://notyourdomain.com/page/, target website will get referer http://notyourdomain.com...
* **rurl.cgi** generates some html with meta-redirect, and target server will get a referer with YOUR DOMAIN. This is useful, when you generating some referral traffic, which is related to your website.

So, finally, mkurl.cgi generates link with url.cgi. You can change it manually to rurl.cgi and place somwhere not within your domain, but refering url will be your domain.


##Disclaimer
Actually, works for me. May be debugging will be required to match your needs.

Handle with care :)
