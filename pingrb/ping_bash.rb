#!/usr/bin/ruby

require 'pp'
require "curses"

dests = ARGV[0].split(',')

count = 3

f_longest = dests.map{|d| d.length}.max

res = {}

include Curses
init_screen

begin
  crmode
  while true do
    threads = []
    
    dests.each do |dest|
      cmd = "ping -t 1 -c#{count} #{dest} | tail -n1"
      #puts cmd

      threads << Thread.new do 
        res = `#{cmd}`
        setpos dests.index(dest), 0
        addstr "#{dest.ljust(f_longest)} #{res}"
      end
    end

    clear

    threads.each do |thread|
      thread.join
    end

    refresh
  end
ensure
  close_screen
end
