#!/usr/bin/perl


use strict;
use CGI qw(param);
use WWW::Shorten::Bitly;

my $bitly_user = "-----put your bitly username here------";
my $bitly_api = "---------------put your bitly key here---------";
my $page_tile = "My link shortener";
my $domain_url = "http://mydomain.com";
my $cgi_location = "/cgi-bin/mkurl.cgi";


my $query = new CGI;

print $query->header;

print $query->start_html($page_tile);

my $url=$query->param('URLValue');


print '<form method="post" action="'.$cgi_location.'" name="URLForm">';
print '<input tabindex="2" id="mkbutton" value="Make URL" type="submit">';
print '<input tabindex="1" maxlength="4096" size="80" id="URLValue" name="URLValue">';
print '</form>';

if ($url)
{

  $url = makeashorterlink($url, $bitly_user, $bitly_api); 

  if ($url)
  {
       $url =~ m/http\:\/\/bit\.ly\/(.*)/;
       my $extracted_url = $1;
        print '<script language="javascript" type="text/javascript">';
        print 'document.URLForm.URLValue.value = "'.$domain_url.$cgi_location.'?'.$extracted_url.'";';
        print 'document.getElementById( "URLValue" ).select();';
        print "</script>";

   }
}

print $query->end_html;

exit;