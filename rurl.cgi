#!/usr/bin/perl -wT

use strict;
use CGI;

#defines

my $err404="/404.php";
###change line above to redirect to your 404 error page

my $q = new CGI;
my $dest;


if (defined ($q->param("keywords")) )
{
   my $short = $q->param("keywords");
  $dest = "http://bit.ly/$short";
  
  print $q->header;
  print "<html>";
  print "<head>";
  print "<meta http-equiv=\"refresh\" content=\"0; url=$dest\" />";
  print "</head>";
  print "<body>";
  print "</body>";
  print "</html>";
  
}
else
{
   $dest=$err404;
   print $q->redirect($dest);
}


1;