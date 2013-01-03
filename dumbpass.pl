#!/usr/bin/perl 
#

# this is the mac os location for the words file ymmv
$DICT = "/usr/share/dict/words";

$NUMCHARS = 5;
$NUMPWS = 5;

open(WORDS, "<$DICT") or die "Cannot open the words file: $DICT\n $!";

my $word = "";
my @all5s = [];
while(<WORDS>) {
  chomp($_);
  if($_ =~ /^[a-z]{5}$/) {
    push(@all5s, $_);
  }
}

# need two rands
#
#
$range = scalar(@all5s) - 1;

for ($i = 0; $i < $NUMPWS; $i++) {
  $rand1 = int(rand($range));
  $rand2 = int(rand($range));

  $pw = $all5s[$rand1] . $all5s[$rand2];
  print "$pw\n";
}
