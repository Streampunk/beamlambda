{
  "targets": [{
    "target_name" : "beamcoder",
    "conditions": [
      ['OS=="linux"', {
        "sources" : [ "src/beamcoder.cc", "src/beamcoder_util.cc",
                      "src/governor.cc", "src/demux.cc",
                      "src/decode.cc", "src/filter.cc",
                      "src/encode.cc", "src/mux.cc",
                      "src/packet.cc", "src/frame.cc",
                      "src/codec_par.cc", "src/format.cc",
                      "src/codec.cc" ],
        "include_dirs": [ "ffmpeg/include" ],
        "defines": [
          "__STDC_CONSTANT_MACROS"
        ],
        "cflags_cc!": [
          "-fno-rtti",
          "-fno-exceptions"
        ],
        "cflags_cc": [
          "-std=c++11",
          "-fexceptions"
        ],
        "link_settings": {
          "libraries": [
            "<@(module_root_dir)/build/Release/libavcodec.so.58",
            "<@(module_root_dir)/build/Release/libavdevice.so.58",
            "<@(module_root_dir)/build/Release/libavfilter.so.7",
            "<@(module_root_dir)/build/Release/libavformat.so.58",
            "<@(module_root_dir)/build/Release/libavutil.so.56",
            "<@(module_root_dir)/build/Release/libfdk-aac.so.2",
            "<@(module_root_dir)/build/Release/libmp3lame.so.0",
            "<@(module_root_dir)/build/Release/libopus.so.0",
            "<@(module_root_dir)/build/Release/libpostproc.so.55",
            "<@(module_root_dir)/build/Release/libswresample.so.3",
            "<@(module_root_dir)/build/Release/libswscale.so.5",
            "<@(module_root_dir)/build/Release/libx264.so.157",
            "<@(module_root_dir)/build/Release/libx265.so.172"
          ],
        "ldflags": [
          "-L<@(module_root_dir)/build/Release",
          "-Wl,-rpath,'$$ORIGIN'",
        ]
      },
      "copies": [
        {
          "destination": "build/Release/",
          "files": [
            "ffmpeg/lib/libavcodec.so.58",
            "ffmpeg/lib/libavdevice.so.58",
            "ffmpeg/lib/libavfilter.so.7",
            "ffmpeg/lib/libavformat.so.58",
            "ffmpeg/lib/libavutil.so.56",
            "ffmpeg/lib/libfdk-aac.so.2",
            "ffmpeg/lib/libmp3lame.so.0",
            "ffmpeg/lib/libopus.so.0",
            "ffmpeg/lib/libpostproc.so.55",
            "ffmpeg/lib/libswresample.so.3",
            "ffmpeg/lib/libswscale.so.5",
            "ffmpeg/lib/libx264.so.157",
            "ffmpeg/lib/libx265.so.172"
          ]
        }
      ]
    }
  ]
  ]
}]
}
