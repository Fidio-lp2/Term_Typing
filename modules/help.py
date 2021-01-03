import curses
import sys

def helpwindow(window):
          help_text = [
                    "<使い方>",
                    "コマンドラインにてmain.pyを実行してください.",
                    "第一引数にAssetsディレクトリに入っているファイルの名前を,パス名無しで指定してください.",
                    "ファイルの指定がない場合は,デフォルトで用意されているHello.javaを使ってもらうことになります.",
                    "[オプション]",
                    "第一引数以降に指定するオプションです。",
                    "-h : ヘルプを表示します.",
                    "-t : 練習中に経過時間を整数で表示します.",
                    "-tt : 練習中に経過時間をコンマ2桁まで表示します.",
                    "-c : 練習中に残りの文字数を表示します.",
                    "-m : ミスタイプの文字数を表示します.",
                    "",
                    "...qで閉じます."
          ]
          for i in range(0,len(help_text),1):
                    window.addstr(i+1,1,help_text[i])
          
          while True:

                    try:
                              key = window.getkey()
                              if key == 'q':
                                        curses.endwin()
                                        sys.exit(0)
                    except curses.error:
                              pass
                    except KeyboardInterrupt:
                              curses.endwin()
                              print("System has been killed.")
                              sys.exit(0)