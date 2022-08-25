#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=flags:|to:|from:).+?(?=\])/).join(",")
