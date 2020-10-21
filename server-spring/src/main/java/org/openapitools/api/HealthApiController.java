package org.openapitools.api;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.context.request.NativeWebRequest;
import java.util.Optional;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2020-10-21T10:20:06.779899-07:00[America/Los_Angeles]")

@Controller
@RequestMapping("${openapi.nLPSandboxDateAnnotator.base-path:/api/v1}")
public class HealthApiController implements HealthApi {

    private final NativeWebRequest request;

    @org.springframework.beans.factory.annotation.Autowired
    public HealthApiController(NativeWebRequest request) {
        this.request = request;
    }

    @Override
    public Optional<NativeWebRequest> getRequest() {
        return Optional.ofNullable(request);
    }

}
