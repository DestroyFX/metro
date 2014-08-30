[section target]

arch: amd64
arch_desc: x86-64bit

[section portage]

CFLAGS: -march=bdver2 -mtune=bdver2 -O2 -pipe -mmmx -mno-3dnow -msse -msse2 -msse3 -mssse3 -msse4a -mcx16 -msahf -mno-movbe -maes -mno-sha -mpclmul -mpopcnt -mabm -mlwp -mfma -mfma4 -mxop -mbmi -mno-bmi2 -mtbm -mavx -mno-avx2 -msse4.2 -msse4.1 -mlzcnt -mno-rtm -mno-hle -mno-rdrnd -mf16c -mno-fsgsbase -mno-rdseed -mprfchw -mno-adx -mfxsr -mxsave -mno-xsaveopt -mno-avx512f -mno-avx512er -mno-avx512cd -mno-avx512pf -mno-prefetchwt1 --param l1-cache-size=16 --param l1-cache-line-size=64 --param l2-cache-size=2048
CHOST: x86_64-pc-linux-gnu
HOSTUSE: mmx sse sse2 sse3 3dnow 3dnowext
