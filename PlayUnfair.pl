#!/usr/bin/perl
use strict;
use warnings;
use List::MoreUtils qw(uniq first_index);

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
if (@plaintext % 2 == 1)
{
    @plaintext = push(@plaintext, "x");
}

#print each letter of message with position in message

for my $j (@plaintext)
{
    print $j;
    #ISSUE: only returns first instance of letter. ex: baby > b0a1b0y3
    #Should return b0a1b2y3
    my $pos = first_index {$_ eq $j} @plaintext;
    print $pos;
}
print "\n";

#print each letter of message with position in alphabet

for my $i (@plaintext)
{
    print $i;
    #return the index of char $i in alphabet
    my $boot = first_index {$_ eq $i} @alphabet;
    print $boot;

#    if even position in plaintext
#    {
#        $boot 
#    }
#    else
#    {
#        something else
#    }
}
print "\n";

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

#print "$letter\n";

# if @plaintext[0..@plaintext] ($#plaintext)



#print "$index @plaintext\n";