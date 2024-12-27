import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.*;
import org.json.JSONArray;
import org.json.JSONObject;

public class HotelReservation {
    private static final String API_HOST = "https://challenge-server.tracks.run/hotel-reservation";

    public static JSONArray searchHotels(String keyword, String checkin, String checkout, int number, String condition) throws Exception {
        String searchEndpoint = API_HOST + "/hotels";
        HttpClient client = HttpClient.newHttpClient();

        URI uri = new URI(searchEndpoint + "?keyword=" + keyword +
                "&checkin=" + checkin +
                "&checkout=" + checkout +
                "&number=" + number +
                "&condition=" + condition);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(uri)
                .header("Content-Type", "application/json")
                .GET()
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new Exception("HTTP Error: " + response.statusCode());
        }

        return new JSONArray(response.body());
    }

    public static JSONObject reserveHotel(String checkin, String checkout, String planId, int number) throws Exception {
        String reservationEndpoint = API_HOST + "/reservations";
        HttpClient client = HttpClient.newHttpClient();

        JSONObject body = new JSONObject();
        body.put("checkin", checkin);
        body.put("checkout", checkout);
        body.put("plan_id", planId);
        body.put("number", number);

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(reservationEndpoint))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(body.toString()))
                .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        if (response.statusCode() != 200) {
            throw new Exception("HTTP Error: " + response.statusCode());
        }

        return new JSONObject(response.body());
    }

    public static void main(String[] args) {
        if (args.length != 5) {
            System.out.println("Usage: java HotelReservation <keyword> <checkin> <checkout> <number> <condition>");
            return;
        }

        String keyword = args[0];
        String checkin = args[1];
        String checkout = args[2];
        int number = Integer.parseInt(args[3]);
        String condition = args[4];

        try {
            // Step 1: Search for hotels
            JSONArray hotels = searchHotels(keyword, checkin, checkout, number, condition);

            if (hotels.isEmpty()) {
                System.out.println("Plan not found.");
                return;
            }

            // Step 2: Select the cheapest plan
            JSONObject cheapestPlan = null;

            for (int i = 0; i < hotels.length(); i++) {
                JSONObject hotel = hotels.getJSONObject(i);
                JSONArray rooms = hotel.optJSONArray("rooms");

                if (rooms != null) {
                    for (int j = 0; j < rooms.length(); j++) {
                        JSONObject room = rooms.getJSONObject(j);
                        JSONArray plans = room.optJSONArray("plans");

                        if (plans != null) {
                            for (int k = 0; k < plans.length(); k++) {
                                JSONObject plan = plans.getJSONObject(k);
                                if (cheapestPlan == null || plan.getInt("price") < cheapestPlan.getInt("price")) {
                                    cheapestPlan = plan;
                                }
                            }
                        }
                    }
                }
            }

            if (cheapestPlan == null) {
                System.out.println("The cheapest plan is fully booked.");
                return;
            }

            // Step 3: Reserve the cheapest plan
            JSONObject reservation = reserveHotel(checkin, checkout, cheapestPlan.getString("id"), number);
            System.out.println("The cheapest plan has been successfully reserved.");
            System.out.println("- reservation id: " + reservation.getString("id"));
            System.out.println("- hotel name: " + reservation.getString("name"));
            System.out.println("- room name: " + reservation.getString("room_name"));
            System.out.println("- plan name: " + reservation.getString("plan_name"));
            System.out.println("- total price: " + reservation.getInt("total"));

        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}