#!/usr/bin/perl -wT

use strict;
use CGI;

my $err404="/404.php";
###change line above to redirect to your 404 error page


my $q = new CGI;
my $dest;

if (defined ($q->param("keywords")) )
{
   my $short = $q->param("keywords");
  $dest = "http://bit.ly/$short";
}
else
{
   $dest=$err404;
}

  print $q->redirect($dest);

1;