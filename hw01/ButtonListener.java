import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class ButtonListener implements MouseListener {
	
	private int numberOfRow;
	private int numberOfColumn;
	private JButton buttonClick;
	private JFrame frame;
	private JPanel buttons;
	
	public ButtonListener(int numberOfRow, int numberOfColumn, JButton buttonClick, JFrame frame, JPanel buttons) {
		this.numberOfRow = numberOfRow;
		this.numberOfColumn = numberOfColumn;
		this.buttonClick = buttonClick;
		this.frame = frame;
		this.buttons = buttons;
	}

	@Override
	public void mouseClicked(MouseEvent arg0) {
		if (this.buttonClick.getText().equals("New Game")) {
			
			EtchMain.initialize(this.numberOfRow, this.numberOfColumn, this.frame, this.buttons);
		} else if (this.buttonClick.getText().equals("Quit")) {
			this.frame.dispose();
		}
		this.frame.repaint();
	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// Auto-generated method stub.

	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// Auto-generated method stub.

	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		// Auto-generated method stub.

	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		// Auto-generated method stub.

	}

}
