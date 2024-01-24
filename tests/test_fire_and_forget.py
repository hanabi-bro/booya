import pytest
import threading
from booya.fire_and_forget import fire_and_forget

# for test_fire_and_forget_decorator
@fire_and_forget
def example_thread(event):
    event.set()

def test_fire_and_forget_decorator():
    event = threading.Event()
    thread = example_thread(event)  # デコレータが適用された関数を実行
    assert isinstance(thread, threading.Thread)  # 新しいスレッドが返されることを確認

    event.wait()  # 関数の実行が完了するのを待つ
    thread.join()
    assert event.is_set()  # 関数が実行されたことを確認

