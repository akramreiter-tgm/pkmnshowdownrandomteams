import java.io.File;
import java.io.RandomAccessFile;
import java.util.ArrayList;
import java.util.HashSet;

import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Teamgenerator extends Application {
	static ArrayList<String> pkmn, pkmnmega, pkmnz;
	public static void main(String[] args) {
		try {
			String zloc = "", megaloc = "", pkmnloc = "";
			System.out.println("hi");
			@SuppressWarnings("resource")
			RandomAccessFile conf = new RandomAccessFile(new File("resources/general.cfg"), "rw");
			System.out.println("hi2");
			try {
				while (zloc.length() == 0 || megaloc.length() == 0 || pkmnloc.length() == 0) {
					String s = conf.readLine();
					System.out.println(s);
					if (s.startsWith("zloc")) zloc = s.substring(s.indexOf(':') + 1);
					if (s.startsWith("megaloc")) megaloc = s.substring(s.indexOf(':') + 1);
					if (s.startsWith("pkmnloc")) pkmnloc = s.substring(s.indexOf(':') + 1);
				}
			}catch (Exception e) {
				e.printStackTrace();
			}
			System.out.println("hi3");
			RandomAccessFile rf = new RandomAccessFile(new File("resources/" + pkmnloc), "rw");
			RandomAccessFile rfm = new RandomAccessFile(new File("resources/" + megaloc), "rw");
			RandomAccessFile rfz = new RandomAccessFile(new File("resources/" + zloc), "rw");
			pkmn = new ArrayList<>();
			pkmnmega = new ArrayList<>();
			pkmnz = new ArrayList<>();
			String s = rf.readLine();
			String temp = "";
			System.out.println("entering loop");
			try {
				while (s.trim().length() > 0) {
					if (!s.startsWith("*")) {
						temp = temp + s + "\n";
					} else {
						pkmn.add(temp.substring(0,temp.length() - 2));
						temp = "";
					}
					s = rf.readLine();
				}
			}catch (Exception e) {
				e.printStackTrace();
			}
			s = rfz.readLine();
			temp = "";
			try {
				while (s.trim().length() > 0) {
					if (!s.startsWith("*")) {
						temp = temp + s + "\n";
					} else {
						pkmnz.add(temp.substring(0,temp.length() - 2));
						temp = "";
					}
					s = rfz.readLine();
				}
			}catch (Exception e) {
				e.printStackTrace();
			}
			s = rfm.readLine();
			temp = "";
			try {
				while (s.trim().length() > 0) {
					if (!s.startsWith("*")) {
						temp = temp + s + "\n";
					} else {
						pkmnmega.add(temp.substring(0,temp.length() - 2));
						temp = "";
					}
					s = rfm.readLine();
				}
			}catch (Exception e) {
				e.printStackTrace();
			}
			Teamgenerator.launch();
		}catch (Exception e) {
			// TODO: handle exception
		}
	}

	@Override
	public void start(Stage primaryStage) throws Exception {
		BorderPane bp = new BorderPane();
		Scene chatScene = new Scene(bp);
		TextArea result = new TextArea(); 
		result.setScrollTop(5);
		primaryStage.setScene(chatScene);
		bp.setCenter(result);
		
		Button generate = new Button("Generate Team");
		final ComboBox<String> zpkmn = new ComboBox<>();
		zpkmn.getItems().addAll(new String[] {"0 Z-Moves", "1 Z-Move", "2 Z-Moves", "Random amount of Z-Moves"});
		zpkmn.getSelectionModel().selectFirst();
		final ComboBox<String> mega = new ComboBox<>();
		mega.getItems().addAll(new String[] {"0 Mega-PKMN", "1 Mega-PKMN", "2 Mega-PKMN", "Random amount of Mega-PKMN"});
		mega.getSelectionModel().selectFirst();
		GridPane gp = new GridPane();
		gp.add(generate, 0, 0);
		gp.add(zpkmn, 0, 1);
		gp.add(mega, 0, 2);
		
		generate.setOnAction(new EventHandler<ActionEvent>() {

			@Override
			public void handle(ActionEvent arg0) {
				String res = "";
				int remain = 6;
				boolean randommega = false;
				boolean randomz = false;
				switch (mega.getSelectionModel().getSelectedItem().toString()) {
				case "1 Mega-PKMN":
					res += pkmnmega.get((int)(Math.random() * pkmnmega.size())) + "\n\n";
					remain -= 1;
					break;
				case "2 Mega-PKMN":
					HashSet<Integer> ids = new HashSet<>();
					while (ids.size() < 2) {
						ids.add((int)(Math.random() * pkmnmega.size()));
					}
					for (Integer i : ids) {
						res += pkmnmega.get(i.intValue()) + "\n\n";
					}
					remain -= 2;
					break;
				case "Random amount of Mega-PKMN": 
					randommega = true;
					break;
				}
				switch (zpkmn.getSelectionModel().getSelectedItem().toString()) {
				case "1 Z-Move":
					res += pkmnz.get((int)(Math.random() * pkmnz.size())) + "\n\n";
					remain -= 1;
					break;
				case "2 Z-Move":
					HashSet<Integer> ids = new HashSet<>();
					while (ids.size() < 2) {
						ids.add((int)(Math.random() * pkmnz.size()));
					}
					for (Integer i : ids) {
						res += pkmnz.get(i.intValue()) + "\n\n";
					}
					remain -= 2;
					break;
				case "Random amount of Z-Moves": 
					randomz = true;
					break;
				}
				
				ArrayList<String> temp = new ArrayList<>();
				temp.addAll(pkmn);
				if (randomz) temp.addAll(pkmnz);
				if (randommega) temp.addAll(pkmnmega);
				HashSet<Integer> ids = new HashSet<>();
				while (ids.size() < remain) {
					ids.add((int)(Math.random() * temp.size()));
				}
				for (Integer i : ids) {
					res += temp.get(i.intValue()) + "\n\n";
				}
				result.setText(res);
			}
		});
		
		bp.setRight(gp);
		primaryStage.show();
		primaryStage.setTitle("Teamgenerator");
	}
}
