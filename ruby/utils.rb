require 'benchmark'

def benchmark
  runs = 100
  
  Benchmark.bmbm do |x|
    x.report { run.times { yield } }
  end

end

def with_utf8_file(filename)
  File.open(filename, 'r:utf-8') do |file|
    yield file.read
  end
end
