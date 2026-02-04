require "artii"

artii = Artii::Base.new
fonts = artii.list_all_fonts.split("\n").sort

puts "=============================="
puts " ASCII Text Generator (Ruby) "
puts "=============================="
puts

puts "Available fonts:"
fonts.each_with_index do |font, index|
  puts "%3d) %s" % [index + 1, font]
end

puts
print "Choose a font (number or name): "
font_input = STDIN.gets.chomp

font =
  if font_input.to_i.between?(1, fonts.length)
    fonts[font_input.to_i - 1]
  elsif fonts.include?(font_input)
    font_input
  else
    "alpha"
  end

puts
print "Enter text to convert: "
text = STDIN.gets.chomp

puts
puts "Font: #{font}"
puts "------------------------------"

art = Artii::Base.new(font: font)
puts art.asciify(text)
