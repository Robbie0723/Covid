
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response
from ask_sdk_model.interfaces.alexa.presentation.apl import RenderDocumentDirective

from apiClass import novelcovid
import launchDisplay as ld
import stats_display as sd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Unsure if i will need to use session attributes at the moment
# session_attr = handler_input.attributes_manager.session_attributes
# data = novelcovid()
# session_attr["data"] = data


data = novelcovid()


def supports_apl(handler_input):
    # type: (HandlerInput) -> bool
    """Check if display is supported by the skill."""
    try:
        if hasattr(handler_input.request_envelope.context.system.device.supported_interfaces, 'alexa_presentation_apl'):
            if(handler_input.request_envelope.context.system.device.supported_interfaces.alexa_presentation_apl is not None):
                return True
            else:
                return False
        else:
            return False
    except:
        return False
        
        
#add graphical component to the skill
def include_display_for_launch(handler_input):
    #APL Directive Code
    if supports_apl(handler_input):
        handler_input.response_builder.add_directive(
            RenderDocumentDirective(
                document=ld.launch_page(),
             datasources=ld.launch_page_data_source()
            )
        )

#add graphical component to the skill
def include_display_for_stats(handler_input, location, cases, active, recovered, deaths):
    #APL Directive Code
    if supports_apl(handler_input):
        handler_input.response_builder.add_directive(
            RenderDocumentDirective(
                document=sd.stats(),
                datasources = sd.stats_datasource(location, cases, active, recovered, deaths)
            )
        )


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome to virus status updates.  We can provide you with current data on the Novel coronavirus status across the  world.  What data are you looking for?"
        include_display_for_launch(handler_input)
        return (handler_input.response_builder.speak(speak_output).ask(speak_output).response)
        


class displayTestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("displayTest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Testing the display"

        return (handler_input.response_builder.speak(speak_output).ask(speak_output).response)


class GetWorldDataIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetWorldDataIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        info = data.get_world_info()
        cases, deaths, recovered, active = info['cases'], info['deaths'], info['recovered'], info['active']
        include_display_for_stats(handler_input, "World Data", cases, active, recovered, deaths)
        
        speak_output = f"""There are a total of {cases} cases.  {active} cases are currently active and {recovered} people have recovered from this virus.
                        {deaths} people have unfortunately died as a result of this virus"""

        return (
            handler_input.response_builder
                .speak(speak_output)
                 .ask("Do you want me to search for something else?")
                 .set_card(SimpleCard("Covid-19", speak_output))
                 .set_should_end_session(False)
                .response
                )
                



class GetCountryDataIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetCountryDataIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        country = handler_input.request_envelope.request.intent.slots['country'].value
        info = data.get_country_info(country)
        
        if len(info) == 1:
            cases, deaths, recovered, active = "unknown", "unknown", "unknown", "unknown"
            speak_output = "There are no known cases of the coronavirus in this country"
        else:
            cases, deaths, recovered, active = info['cases'], info['deaths'], info['recovered'], info['active']
            if recovered > 0:
                recovered_pronoun = "people have"
            elif recovered == 0:
                pronoun = "person has"
            if deaths > 1:
                death_pronoun = "people have"
            elif deaths == 1:
                death_pronoun = "person has"
            
            speak_output = f"""There are a total of {cases} cases in this country.  {active} cases are currently active. and {recovered} {recovered_pronoun} recovered from this virus.
                        {deaths} {death_pronoun} unfortunately died as a result of this virus """
        include_display_for_stats(handler_input, "Country: " + country.title(), cases, active, recovered, deaths)

                        
        return (
            handler_input.response_builder
                .speak(speak_output)
                 .ask("Do you want me to search for something else?")
                 .set_card(SimpleCard("Covid-19", speak_output))
                .set_should_end_session(False) 
                .response
        )



class GetStateDataIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetStateDataIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        state = handler_input.request_envelope.request.intent.slots['state'].value
        info = data.get_state_info(state)
        cases, deaths, active, recovered = info['cases'], info['deaths'], info['active'], "unknown"
        

        if deaths > 1:
            death_pronoun = "people have"
        elif deaths == 1:
            death_pronoun = "person has"

        speak_output = f"""There are a total of {cases} confirmed cases.  {active} cases are currently active.
                        {deaths} {death_pronoun} unfortunately died as a result of this virus."""
        
        include_display_for_stats(handler_input, "United States of America: " + state, cases, active, recovered, deaths)
        

        return (
            handler_input.response_builder
                .speak(speak_output)
                 .ask("Do you want me to search for something else?")
                 .set_card(SimpleCard("Covid-19", speak_output))
                .set_should_end_session(False)
                .response
        )




class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "We can tell you about the status in states in America, different countries, or the status of all cases in the world.  Just tell us what you would like to hear."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Thank you for visiting.  Stay safe."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response



class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(GetWorldDataIntentHandler())
sb.add_request_handler(GetCountryDataIntentHandler())
sb.add_request_handler(GetStateDataIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()