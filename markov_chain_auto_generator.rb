require 'json'
require 'pp'

iv = [
[1, 8, 8],

[2, 1, 0, 8, 8],
[2, 0, 1, 0, 0, 8, 8],

[0, 2, 0, 1, 0, 0, 0, 8, 8],
[0, 2, 0, 0, 1, 0, 0, 0, 0, 8, 8],
[0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 8, 8],
[0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 8, 8],

[3, 0, 0, 2, 0, 0, 0, 1],
[3, 0, 0, 2, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 2, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1],
[3, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1],
]

nodes = 2 ** 4 - 2
half = nodes / 2

str_self    = 0

str_parent  = 2 ** 4
str_child   = 2 ** 4

str_sibling = 2 ** 3

str_uncle   = 2 ** 2
str_cousin  = 2 ** 2

str_root    = 0

str_god     = 0

iv = []
(0..nodes).each do |i|
  if i < half then
    child_pos = (i + 1) * 2 - 1
    child_rpos = child_pos + 1
    max = child_rpos
  else 
    max = i
  end

  ivi = [0] * max

  if i < half then
    ivi[child_pos]  = str_child
    ivi[child_rpos] = str_child
  end

  if i > 0 then
    ivi[0] = str_god * ((i - 1) / 2)

    i_parent = (i - 1) / 2
    ivi[i_parent] = str_parent

    if i % 2 == 1 then
      i_sibling = i + 1
    else 
      i_sibling = i - 1
    end

    ivi[i_sibling] = str_sibling

    if i_parent > 0 then
      if i_parent % 2 == 1 then
        i_uncle = i_parent + 1
      else
        i_uncle = i_parent - 1
      end

      ivi[i_uncle] = str_uncle

      i_cousin = (i_uncle + 1) * 2 - 1
      ivi[i_cousin]     = str_cousin
      ivi[i_cousin + 1] = str_cousin
    end

  end

  ivi[i] = str_self

  iv[i] = ivi
end

#<<-CBLK
puts '['
iv.each do |d|
  puts '[' + d.join(',') + ']'
end
puts ']'
#CBLK

target = iv.reduce(0) do |a, e|
  l = e.length
  if l > a then
    l
  else
    a
  end
end

while iv.length < target do
  iv << []
end

iv.each do |d|
  while d.length < target do
    d << 0
  end

  sum = d.reduce(0) do |a, e|
    a += e
  end

  if sum == 0 then
    # array of zeros
    fill = 1.0 / target
    fill = 0
    d.each_index do |i|
      d[i] = fill.round(12)
    end
  else 
    d.each_index do |i|
      d[i] = d[i].to_f / sum
    end
  end
end


puts JSON.dump(iv)
