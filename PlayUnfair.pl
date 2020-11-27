#!/usr/bin/perl
use strict;
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
$codeword =~ s/z/x/g;

my @key = split //, $codeword;
#adds key to beginning of alphabet
unshift (@alphabet, @key);
#removes repeated characters from key alphabet
@alphabet = uniq(@alphabet);

print "enter a message: ";
my $message = <STDIN>;
chomp $message;
#removes whitespace
$message =~ s/\s+//g;
$message =~ s/z/x/g;
my @plaintext = split //, $message;

if (@plaintext % 2 == 1)
{
    push(@plaintext, "x");
}

my $ciphertext;

#$i gets numbers 0-$#plaintext
for my $i (0..$#plaintext)
{
    #letter at each $i
    my $letr = $plaintext[$i];
    #location of each letter in @alphabet
    my $idx = first_index {$_ eq $plaintext[$i]} @alphabet;
    my $eChar;

    #Letters in same column aren't swapped--need fix
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
        if ($eChar eq $plaintext[$i])
        {
            $eChar = $plaintext[$i + 1]
        }
        $ciphertext .= $eChar;
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
        if ($eChar eq $plaintext[$i])
        {
            $eChar = $plaintext[$i - 1]
        }
        $ciphertext .= $eChar;
    }
}
print "$ciphertext\n";