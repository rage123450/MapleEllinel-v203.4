package loaders;

import client.life.DropInfo;
import constants.ServerConstants;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import util.Util;
import util.XMLApi;

import java.io.*;
import java.util.*;

/**
 * Created on 2/21/2018.
 */
public class DropData {

    private static Map<Integer, Set<DropInfo>> drops = new HashMap<>();

    public static void loadDropsFromWz() {
        String wzDir = ServerConstants.WZ_DIR + "\\String.wz\\MonsterBook.img.xml";
        File file = new File(wzDir);
        Document doc = XMLApi.getRoot(file);
        Node mainNode = XMLApi.getAllChildren(doc).get(0);
        for(Node node : XMLApi.getAllChildren(mainNode)) {
            int mobID = Integer.parseInt(XMLApi.getAttributes(node).get("name").replace(".img", ""));
            Node rewardNode = XMLApi.getFirstChildByNameBF(node, "reward");
            if(rewardNode != null) {
                for(Node reward : XMLApi.getAllChildren(rewardNode)) {
                    int rewardID = Integer.parseInt(XMLApi.getNamedAttribute(reward, "value"));
                    DropInfo dropInfo = new DropInfo(rewardID, 0, 100, 0); // default vals, 10% chance to drop
                    addDrop(mobID, dropInfo);
                }
            }
        }
    }

    public static void saveDropsToTxt(File file) {
        try {
            PrintWriter das = new PrintWriter(new FileOutputStream(file));
            for (Map.Entry<Integer, Set<DropInfo>> entry : getDrops().entrySet()) {
                int mobID = entry.getKey();
                Set<DropInfo> drops = entry.getValue();
                das.println(mobID);
                for (DropInfo di : drops) {
                    if (di.getQuestReq() == 0) {
                        das.println(String.format("%d %d", di.getItemID(), di.getChance()));
                    } else {
                        das.println(String.format("%d %d %d", di.getItemID(), di.getChance(), di.getQuestReq()));
                    }
                }
                das.println();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void loadCompleteDropsFromTxt(File file) {
        try {
            Scanner scanner = new Scanner(new FileInputStream(file));
            int mobID = 0;
            while(scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] split = line.split(" ");
                /*
                Format, either:
                mobID (int)
                or:
                itemID (int) chance (int out of 1000) questReq?(int)
                So, single line = mobID, else 2/3 ints
                 */
                if(split.length == 1 && !split[0].equals("")) {
                    mobID = Integer.parseInt(split[0]);
                } else if(split.length >= 2) {
                    int itemID = Integer.parseInt(split[0]);
                    int chance = Integer.parseInt(split[1]);
                    int questReq = 0;
                    if(split.length >= 3) {
                        questReq = Integer.parseInt(split[2]);
                    }
                    DropInfo dropInfo = new DropInfo(itemID, 0, chance, questReq);
                    addDrop(mobID, dropInfo);
                }

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void saveDropsToDat(String dir) {
        Util.makeDirIfAbsent(dir);
        for (Map.Entry<Integer, Set<DropInfo>> entry : getDrops().entrySet()) {
            int mobID = entry.getKey();
            Set<DropInfo> drops = entry.getValue();
            File file = new File(String.format("%s\\%d.dat", dir, mobID));
            try {
                DataOutputStream das = new DataOutputStream(new FileOutputStream(file));
                das.writeInt(mobID);
                das.writeShort(drops.size());
                for(DropInfo dropInfo : drops) {
                    das.writeInt(dropInfo.getItemID());
                    das.writeInt(dropInfo.getChance());
                    das.writeInt(dropInfo.getQuestReq());
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static Set<DropInfo> getDropInfoByID(int mobID) {
        Set<DropInfo> drops = getCachedDropInfoById(mobID);
        if(drops == null) {
            File file = new File(String.format("%s\\mobDrops\\%d.dat", ServerConstants.DAT_DIR, mobID));
            if (file.exists()) {
                return loadDropsFromFile(file);
            }
            return null;
        }
        return drops;
    }

    private static Set<DropInfo> getCachedDropInfoById(int mobID) {
        return getDrops().getOrDefault(mobID, null);
    }

    public static Set<DropInfo> loadDropsFromFile(File file) {
        Set<DropInfo> drops = null;
        try {
            DataInputStream dis = new DataInputStream(new FileInputStream(file));
            int mobID = dis.readInt();
            short size = dis.readShort();
            drops = new HashSet<>();
            for (int i = 0; i < size; i++) {
                DropInfo dropInfo = new DropInfo();
                dropInfo.setItemID(dis.readInt());
                dropInfo.setChance(dis.readInt());
                dropInfo.setQuestReq(dis.readInt());
                addDrop(mobID, dropInfo);
                drops.add(dropInfo);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return drops;
    }

    private static void addDrop(int mobID, DropInfo dropInfo) {
        if(!getDrops().containsKey(mobID)) {
            getDrops().put(mobID, new HashSet<>());
        }
        getDrops().get(mobID).add(dropInfo);
    }

    private static Map<Integer, Set<DropInfo>> getDrops() {
        return drops;
    }

    public static void generateTxtFromMonsterBook() {
        loadDropsFromWz();
        saveDropsToTxt(new File(ServerConstants.RESOURCES_DIR + "\\mobDrops.txt"));
    }

    public static void generateDatFiles() {
        loadCompleteDropsFromTxt(new File(ServerConstants.RESOURCES_DIR + "\\mobDrops.txt"));
        saveDropsToDat(ServerConstants.DAT_DIR + "\\mobDrops");
    }

    public static void main(String[] args) {
        Set<DropInfo> drops = getDropInfoByID(4230113);
        System.out.println(drops);
    }
}