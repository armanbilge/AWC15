require 'rake/clean'

PDFLATEX = 'pdflatex'

TEX = FileList['*.tex']
AUX = TEX.ext('aux')
LOG = TEX.ext('log')
OUT = TEX.ext('out')
PDF = TEX.ext('pdf')

CLEAN << AUX
CLEAN << LOG
CLEAN << OUT
CLOBBER << PDF

task :default => PDF

rule '.pdf' => '.tex' do |t|
  2.times do
    sh "#{PDFLATEX} #{t.name.pathmap('%n')}"
  end
end
