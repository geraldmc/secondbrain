from secondbrain.app import main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from secondbrain!" in captured.err
