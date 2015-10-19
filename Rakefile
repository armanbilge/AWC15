require 'rake/clean'

PDFLATEX = 'pdflatex'

TEX = FileList['*.tex']
AUX = TEX.ext('aux')
LOG = TEX.ext('log')
NAV = TEX.ext('nav')
OUT = TEX.ext('out')
PDF = TEX.ext('pdf')
SNM = TEX.ext('snm')
TOC = TEX.ext('toc')

CLEAN << AUX
CLEAN << LOG
CLEAN << NAV
CLEAN << OUT
CLEAN << SNM
CLEAN << TOC
CLOBBER << PDF

task :default => PDF

rule '.pdf' => '.tex' do |t|
  2.times do
    sh "#{PDFLATEX} #{t.name.pathmap('%n')}"
  end
end
