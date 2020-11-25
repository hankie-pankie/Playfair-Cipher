#!/usr/bin/perl
#use strict;
use warnings;
use List::MoreUtils qw(uniq first_index);
use POSIX qw(floor);

#Perl Playfair Cipher Algorithm

my @alphabet = qw(a b c d e f g h i j k l m n o p q r s t u v w x y);

print "enter a codeword: ";
my $codeword = <STDIN>;
chomp $codeword;
$codeword =~ tr/A-Z/a-z/;
#removes whitespace
$codeword =~ s/\s+//g;

my @key = split //, $codeword;
#adds key to beginning of alphabet
unshift (@alphabet, @key);
#removes repeated characters from keyalphabet
@alphabet = uniq(@alphabet);

print "@alphabet[0..$#alphabet]\n";

#need to neaten up codeword

print "enter a message: ";
my $message = <STDIN>;
chomp $message;
#removes whitespace
$message =~ s/\s+//g;
my @plaintext = split //, $message;
#maybe create a hash given @plaintext 
#each letter would get a number position assigned
#Hash probably wouldn't do well with repeated letters having 2 positions

#Doesn't work for some reason
if (@plaintext % 2 == 1)
{
    @plaintext = push(@plaintext, "x");
}

#$i gets numbers 0-$#plaintext
for my $i (0..$#plaintext)
{
    #letter at each $i
    my $letr = $plaintext[$i];
    #location of each letter in @alphabet
    my $idx = first_index {$_ eq $plaintext[$i]} @alphabet;

    if ($i % 2 == 0)
    {
        my $posPlus = first_index {$_ eq $plaintext[$i + 1]} @alphabet;
        my $edx = 5 * (floor($idx / 5)) + $posPlus - 5 * (floor($posPlus / 5));
        if ($edx > 24)
        {
            $edx = $edx - 24;
        }
        if ($edx < 0)
        {
            $edx = $edx + 24;
        }
        $eChar = $alphabet[$edx];
    }
    else
    {
        my $posNeg = first_index {$_ eq $plaintext[$i - 1]} @alphabet;
        my $edx = 5 * (floor($idx / 5)) + $posNeg - 5 * (floor($posNeg / 5));
        if ($edx > 24)
        {
            $edx = $edx - 24;
        }
        if ($edx < 0)
        {
            $edx = $edx + 24;
        }
        $eChar = $alphabet[$edx];
    }

    print "$i: $letr $idx $eChar\n";

}

#THIS GOOD
#my @i = first_index {$_ eq @plaintext[0..$#plaintext]} @alphabet;
#print "@i\n";

#Maybe but not as gud
#'h' isn't numeric. Needs other equivalence operator...
#my @i = grep { $alphabet[$_] eq "h"} 0..$#alphabet;
#print :"@i\n";

#print first_index {}

#my $index = "$codeword$alphabet";

#my $pos = 5;
#my $letter = $plaintext[$pos];